from __future__ import annotations

import base64
import json
import math
import re
from array import array
from pathlib import Path

import shapefile


WORKDIR = Path(__file__).resolve().parent
SOURCE_PREFIX = WORKDIR / "NhaHat_Footprint"
OUTPUT_GLTF = WORKDIR / "NhaHat_ThanhPho_LoD3.gltf"
OUTPUT_GEOJSON = WORKDIR / "NhaHat_ThanhPho_LoD3.geojson"


def parse_height(value: object, default: float = 26.0) -> float:
    if value is None:
        return default
    text = str(value).strip()
    if not text:
        return default
    match = re.search(r"-?\d+(?:\.\d+)?", text.replace(",", "."))
    return float(match.group(0)) if match else default


def lonlat_to_local(points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    lon0 = sum(lon for lon, _ in points) / len(points)
    lat0 = sum(lat for _, lat in points) / len(points)
    meters_per_degree_lat = 110540.0
    meters_per_degree_lon = 111320.0 * math.cos(math.radians(lat0))

    projected = []
    for lon, lat in points:
        x = (lon - lon0) * meters_per_degree_lon
        z = (lat - lat0) * meters_per_degree_lat
        projected.append((x, z))
    return projected


def polygon_area(points: list[tuple[float, float]]) -> float:
    area = 0.0
    for index in range(len(points)):
        x1, y1 = points[index]
        x2, y2 = points[(index + 1) % len(points)]
        area += x1 * y2 - x2 * y1
    return area / 2.0


def ensure_ccw(points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    return points if polygon_area(points) > 0 else list(reversed(points))


def cross_z(a: tuple[float, float], b: tuple[float, float], c: tuple[float, float]) -> float:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def point_in_triangle(point: tuple[float, float], a, b, c) -> bool:
    px, py = point
    ax, ay = a
    bx, by = b
    cx, cy = c
    v0x, v0y = cx - ax, cy - ay
    v1x, v1y = bx - ax, by - ay
    v2x, v2y = px - ax, py - ay

    dot00 = v0x * v0x + v0y * v0y
    dot01 = v0x * v1x + v0y * v1y
    dot02 = v0x * v2x + v0y * v2y
    dot11 = v1x * v1x + v1y * v1y
    dot12 = v1x * v2x + v1y * v2y

    denom = dot00 * dot11 - dot01 * dot01
    if abs(denom) < 1e-12:
        return False
    inv = 1.0 / denom
    u = (dot11 * dot02 - dot01 * dot12) * inv
    v = (dot00 * dot12 - dot01 * dot02) * inv
    return u >= -1e-10 and v >= -1e-10 and u + v <= 1.0 + 1e-10


def triangulate_polygon(points: list[tuple[float, float]]) -> list[tuple[int, int, int]]:
    vertices = ensure_ccw(points)
    indices = list(range(len(vertices)))
    triangles: list[tuple[int, int, int]] = []

    guard = 0
    while len(indices) > 3 and guard < 10_000:
        ear_found = False
        guard += 1
        for offset in range(len(indices)):
            prev_index = indices[(offset - 1) % len(indices)]
            curr_index = indices[offset]
            next_index = indices[(offset + 1) % len(indices)]

            a = vertices[prev_index]
            b = vertices[curr_index]
            c = vertices[next_index]
            if cross_z(a, b, c) <= 0:
                continue

            is_ear = True
            for other_index in indices:
                if other_index in (prev_index, curr_index, next_index):
                    continue
                if point_in_triangle(vertices[other_index], a, b, c):
                    is_ear = False
                    break

            if is_ear:
                triangles.append((prev_index, curr_index, next_index))
                del indices[offset]
                ear_found = True
                break

        if not ear_found:
            break

    if len(indices) == 3:
        triangles.append((indices[0], indices[1], indices[2]))

    if len(triangles) < len(vertices) - 2:
        raise ValueError("Failed to triangulate footprint polygon.")

    return triangles


def scale_ring(points: list[tuple[float, float]], scale: float) -> list[tuple[float, float]]:
    centroid_x = sum(x for x, _ in points) / len(points)
    centroid_z = sum(z for _, z in points) / len(points)
    return [
        (centroid_x + (x - centroid_x) * scale, centroid_z + (z - centroid_z) * scale)
        for x, z in points
    ]


def build_tiered_rings(points: list[tuple[float, float]], total_height: float) -> list[tuple[str, float, list[tuple[float, float]]]]:
    profile = [
        ("base", 0.00, 1.00),
        ("podium", 0.18, 1.03),
        ("body_lower", 0.42, 0.97),
        ("body_mid", 0.68, 0.90),
        ("body_upper", 0.88, 0.84),
        ("roof", 1.00, 0.79),
    ]
    return [
        (name, total_height * height_ratio, scale_ring(points, scale))
        for name, height_ratio, scale in profile
    ]


def add_vertex(vertices: list[tuple[float, float, float]], vertex_map: dict[tuple[float, float, float], int], vertex: tuple[float, float, float]) -> int:
    key = (round(vertex[0], 6), round(vertex[1], 6), round(vertex[2], 6))
    if key not in vertex_map:
        vertex_map[key] = len(vertices)
        vertices.append(key)
    return vertex_map[key]


def build_mesh(rings: list[tuple[str, float, list[tuple[float, float]]]]) -> tuple[list[tuple[float, float, float]], dict[str, list[tuple[int, int, int]]]]:
    vertices: list[tuple[float, float, float]] = []
    vertex_map: dict[tuple[float, float, float], int] = {}
    face_groups: dict[str, list[tuple[int, int, int]]] = {"bottom": [], "roof": []}

    ring_indices: list[list[int]] = []
    for _, height, ring in rings:
        ring_indices.append([
            add_vertex(vertices, vertex_map, (x, height, z))
            for x, z in ring
        ])

    bottom_ring = rings[0][2]
    bottom_triangles = triangulate_polygon(bottom_ring)
    for a, b, c in bottom_triangles:
        face_groups["bottom"].append((ring_indices[0][a], ring_indices[0][c], ring_indices[0][b]))

    for level_index in range(len(rings) - 1):
        lower = ring_indices[level_index]
        upper = ring_indices[level_index + 1]
        side_group = f"side_{rings[level_index + 1][0]}"
        face_groups.setdefault(side_group, [])
        count = len(lower)
        for point_index in range(count):
            next_index = (point_index + 1) % count
            a = lower[point_index]
            b = lower[next_index]
            c = upper[next_index]
            d = upper[point_index]
            face_groups[side_group].append((a, b, c))
            face_groups[side_group].append((a, c, d))

    top_ring = rings[-1][2]
    top_triangles = triangulate_polygon(top_ring)
    for a, b, c in top_triangles:
        face_groups["roof"].append((ring_indices[-1][a], ring_indices[-1][b], ring_indices[-1][c]))

    return vertices, face_groups


def compute_vertex_normals(vertices: list[tuple[float, float, float]], faces: list[tuple[int, int, int]]) -> list[tuple[float, float, float]]:
    normals = [[0.0, 0.0, 0.0] for _ in vertices]
    for i1, i2, i3 in faces:
        x1, y1, z1 = vertices[i1]
        x2, y2, z2 = vertices[i2]
        x3, y3, z3 = vertices[i3]
        ux, uy, uz = x2 - x1, y2 - y1, z2 - z1
        vx, vy, vz = x3 - x1, y3 - y1, z3 - z1
        nx = uy * vz - uz * vy
        ny = uz * vx - ux * vz
        nz = ux * vy - uy * vx
        length = math.sqrt(nx * nx + ny * ny + nz * nz)
        if length == 0:
            continue
        nx /= length
        ny /= length
        nz /= length
        for index in (i1, i2, i3):
            normals[index][0] += nx
            normals[index][1] += ny
            normals[index][2] += nz

    result = []
    for nx, ny, nz in normals:
        length = math.sqrt(nx * nx + ny * ny + nz * nz)
        if length == 0:
            result.append((0.0, 1.0, 0.0))
        else:
            result.append((nx / length, ny / length, nz / length))
    return result


def pack_accessor(values: list[tuple[float, ...]], component_type: str) -> tuple[bytes, int]:
    if component_type == "float32":
        flat = array("f")
        for row in values:
            flat.extend(row)
        return flat.tobytes(), 5126
    if component_type == "uint16":
        flat = array("H")
        for row in values:
            flat.extend(row)
        return flat.tobytes(), 5123
    if component_type == "uint32":
        flat = array("I")
        for row in values:
            flat.extend(row)
        return flat.tobytes(), 5125
    raise ValueError(f"Unsupported component type: {component_type}")


def build_gltf(
    vertices: list[tuple[float, float, float]],
    normals: list[tuple[float, float, float]],
    face_groups: dict[str, list[tuple[int, int, int]]],
    name: str,
    total_height: float,
) -> dict:
    position_bytes, position_component_type = pack_accessor(vertices, "float32")
    normal_bytes, normal_component_type = pack_accessor(normals, "float32")

    position_count = len(vertices)

    def pad(data: bytes) -> bytes:
        while len(data) % 4:
            data += b"\x00"
        return data

    padded_positions = pad(position_bytes)
    padded_normals = pad(normal_bytes)
    position_offset = 0
    normal_offset = len(padded_positions)
    buffer_chunks = [padded_positions, padded_normals]
    buffer_views = [
        {"buffer": 0, "byteOffset": position_offset, "byteLength": len(padded_positions), "target": 34962},
        {"buffer": 0, "byteOffset": normal_offset, "byteLength": len(padded_normals), "target": 34962},
    ]
    accessors = [
        {
            "bufferView": 0,
            "componentType": position_component_type,
            "count": position_count,
            "type": "VEC3",
            "min": [min(vertex[0] for vertex in vertices), min(vertex[1] for vertex in vertices), min(vertex[2] for vertex in vertices)],
            "max": [max(vertex[0] for vertex in vertices), max(vertex[1] for vertex in vertices), max(vertex[2] for vertex in vertices)],
        },
        {
            "bufferView": 1,
            "componentType": normal_component_type,
            "count": position_count,
            "type": "VEC3",
            "min": [-1.0, -1.0, -1.0],
            "max": [1.0, 1.0, 1.0],
        },
    ]

    material_by_group = {
        "bottom": 0,
        "side_podium": 1,
        "side_body_lower": 2,
        "side_body_mid": 3,
        "side_body_upper": 4,
        "side_roof": 5,
        "roof": 6,
    }

    materials = [
        {
            "name": "BasementStone",
            "pbrMetallicRoughness": {"baseColorFactor": [0.33, 0.30, 0.28, 1.0], "metallicFactor": 0.0, "roughnessFactor": 0.95},
        },
        {
            "name": "PodiumCream",
            "pbrMetallicRoughness": {"baseColorFactor": [0.83, 0.76, 0.63, 1.0], "metallicFactor": 0.05, "roughnessFactor": 0.82},
        },
        {
            "name": "BodyLowerRose",
            "pbrMetallicRoughness": {"baseColorFactor": [0.78, 0.45, 0.44, 1.0], "metallicFactor": 0.12, "roughnessFactor": 0.70},
        },
        {
            "name": "BodyMidBrick",
            "pbrMetallicRoughness": {"baseColorFactor": [0.67, 0.32, 0.31, 1.0], "metallicFactor": 0.15, "roughnessFactor": 0.64},
        },
        {
            "name": "BodyUpperTerracotta",
            "pbrMetallicRoughness": {"baseColorFactor": [0.58, 0.24, 0.25, 1.0], "metallicFactor": 0.18, "roughnessFactor": 0.58},
        },
        {
            "name": "RoofDrum",
            "pbrMetallicRoughness": {"baseColorFactor": [0.73, 0.66, 0.55, 1.0], "metallicFactor": 0.12, "roughnessFactor": 0.62},
        },
        {
            "name": "RoofTop",
            "pbrMetallicRoughness": {"baseColorFactor": [0.86, 0.80, 0.71, 1.0], "metallicFactor": 0.08, "roughnessFactor": 0.72},
        },
    ]

    primitives = []
    group_order = [
        "bottom",
        "side_podium",
        "side_body_lower",
        "side_body_mid",
        "side_body_upper",
        "side_roof",
        "roof",
    ]
    max_index = len(vertices) - 1
    index_component = "uint32" if max_index > 65535 else "uint16"

    byte_cursor = len(padded_positions) + len(padded_normals)
    for group_name in group_order:
        group_faces = face_groups.get(group_name, [])
        if not group_faces:
            continue
        index_bytes, index_component_type = pack_accessor(group_faces, index_component)
        padded_indices = pad(index_bytes)
        buffer_chunks.append(padded_indices)

        view_index = len(buffer_views)
        buffer_views.append({"buffer": 0, "byteOffset": byte_cursor, "byteLength": len(padded_indices), "target": 34963})
        byte_cursor += len(padded_indices)

        accessor_index = len(accessors)
        accessors.append(
            {
                "bufferView": view_index,
                "componentType": index_component_type,
                "count": len(group_faces) * 3,
                "type": "SCALAR",
                "min": [0],
                "max": [max_index],
            }
        )

        primitives.append(
            {
                "mode": 4,
                "attributes": {"POSITION": 0, "NORMAL": 1},
                "indices": accessor_index,
                "material": material_by_group.get(group_name, 2),
            }
        )

    buffer_data = b"".join(buffer_chunks)
    encoded_buffer = base64.b64encode(buffer_data).decode("ascii")

    return {
        "asset": {"version": "2.0", "generator": "LAB2 LoD3 footprint extruder"},
        "scene": 0,
        "scenes": [{"nodes": [0]}],
        "nodes": [{"mesh": 0, "name": name, "extras": {"height_m": total_height}}],
        "meshes": [
            {
                "name": name,
                "primitives": primitives,
            }
        ],
        "materials": materials,
        "buffers": [{"byteLength": len(buffer_data), "uri": f"data:application/octet-stream;base64,{encoded_buffer}"}],
        "bufferViews": buffer_views,
        "accessors": accessors,
    }


def export_geojson(rings: list[tuple[str, float, list[tuple[float, float]]]], total_height: float, name: str) -> dict:
    features = []
    for level_name, z_height, ring in rings:
        coordinates = [[list(point) for point in ring + [ring[0]]]]
        features.append(
            {
                "type": "Feature",
                "properties": {
                    "name": name,
                    "part": level_name,
                    "height_m": round(z_height, 3),
                    "total_height_m": round(total_height, 3),
                },
                "geometry": {"type": "Polygon", "coordinates": coordinates},
            }
        )
    return {"type": "FeatureCollection", "features": features}


def main() -> None:
    reader = shapefile.Reader(str(SOURCE_PREFIX))
    fields = [field[0] for field in reader.fields[1:]]
    record = reader.record(0)
    shape = reader.shape(0)

    name_index = fields.index("name_vi") if "name_vi" in fields else fields.index("name")
    name = str(record[name_index]).strip() or "Nha Hat Thanh Pho"
    height_index = fields.index("height") if "height" in fields else None
    total_height = parse_height(record[height_index] if height_index is not None else None)

    raw_points = shape.points[:]
    if raw_points and raw_points[0] == raw_points[-1]:
        raw_points = raw_points[:-1]

    local_points = ensure_ccw(lonlat_to_local(raw_points))
    rings = build_tiered_rings(local_points, total_height)
    vertices, face_groups = build_mesh(rings)
    all_faces: list[tuple[int, int, int]] = [face for group in face_groups.values() for face in group]
    normals = compute_vertex_normals(vertices, all_faces)

    gltf = build_gltf(vertices, normals, face_groups, name, total_height)
    geojson = export_geojson(rings, total_height, name)

    OUTPUT_GLTF.write_text(json.dumps(gltf, ensure_ascii=False, indent=2), encoding="utf-8")
    OUTPUT_GEOJSON.write_text(json.dumps(geojson, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Generated {OUTPUT_GLTF.name} with {len(vertices)} vertices and {len(all_faces)} triangles.")
    print(f"Generated {OUTPUT_GEOJSON.name} with {len(rings)} stacked footprint levels.")


if __name__ == "__main__":
    main()