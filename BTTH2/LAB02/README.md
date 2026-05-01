# GIS Lab 02 - Nhà hát Thành phố Hồ Chí Minh

Đây là project nộp Lab 02 môn GIS. Nhóm chọn **Nhà hát Thành phố Hồ Chí Minh** và biểu diễn mô hình kiến trúc mức **LoD3** trên bản đồ 3D bằng **ArcGIS Maps SDK for JavaScript**.

## Mở Bài Demo Chính

Chạy local server tại thư mục project:

```bash
python3 -m http.server 8080
```

Sau đó mở:

```text
http://localhost:8080
```

File demo chính là:

```text
index.html
```

## Nhóm đã đảm bảo yêu cầu của Lab02

- **Thu thập dữ liệu JSON/GeoJSON:** có footprint, GeoJSON tầng khối, metadata LoD3 và shapefile gốc trong `data/`.
- **Biểu diễn trên bản đồ 3D ArcGIS JS:** `index.html` dùng `SceneView`, `GraphicsLayer`, `Polygon`, `ExtrudeSymbol3DLayer` và `ground: "world-elevation"`.
- **Công trình nổi tiếng:** Nhà hát Thành phố Hồ Chí Minh, số 7 Công trường Lam Sơn, Quận 1, TP.HCM.
- **Mức độ chi tiết LoD3:** tách khối chính, khối phụ, mái, cửa, cửa sổ, ban công, gờ nổi và chi tiết mặt đứng.
- **Có tài liệu nộp:** đề bài, phân công, báo cáo tóm tắt, hướng dẫn chạy và nguồn tham khảo trong `docs/`.

## Cấu Trúc Chính

```text
LAB02/
├── index.html                         # Demo chính để nộp/demonstrate
├── data/                              # Dữ liệu không gian và mô hình
│   ├── geojson/                       # Footprint và GeoJSON LoD3
│   ├── model/                         # glTF/GLB model
│   └── shapefile/                     # Shapefile footprint gốc
├── viewers/                           # Các viewer phụ để kiểm tra dữ liệu
├── scripts/                           # Script dựng/xuất dữ liệu
├── docs/                              # Tài liệu bài làm, phân công, nguồn
├── screenshots/                       # Ảnh kết quả
└── HUONG_DAN.txt                      # Hướng dẫn chạy nhanh
```

Xem chi tiết từng file tại:

```text
docs/STRUCTURE.md
```

## Các Trang Có Thể Mở

| Trang                                | Vai trò                                                          |
| ------------------------------------ | ----------------------------------------------------------------- |
| `index.html`                       | Demo chính bằng ArcGIS SceneView, nên dùng để nộp và demo |
| `viewers/geojson_layer_check.html` | Kiểm tra GeoJSON tầng khối bằng ArcGIS `GeoJSONLayer`       |
| `viewers/gltf_lod3_check.html`     | Kiểm tra model glTF dựng từ footprint                          |
| `viewers/reference_model.html`     | Xem model SketchUp tham chiếu đã export sang GLB               |

## Tài Liệu Nên Đọc 

- `docs/STRUCTURE.md`: bản đồ cấu trúc folder.
- `docs/bao_cao_tom_tat.md`: tóm tắt quy trình và kết quả.
- `docs/phan_cong_LAB2.csv`: phân công công việc nhóm.
