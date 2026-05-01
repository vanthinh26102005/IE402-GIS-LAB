## Mục tiêu

Phần này dựng khối chính từ footprint của công trình, xử lý extrusion theo chiều cao 26 m, chia thành các tầng khối và xuất ra mô hình 3D LoD3 cho phần thân.

## Đầu ra

- `NhaHat_ThanhPho_LoD3.gltf`: mô hình 3D dùng cho trình xem glTF
- `NhaHat_ThanhPho_LoD3.geojson`: các lớp footprint theo tầng để kiểm tra hình học

## Cách chạy

```bash
python build_nhathanhpho_lod3.py
```

## Ý tưởng dựng khối

1. Đọc footprint từ shapefile.
2. Chuyển tọa độ địa lý sang hệ tọa độ cục bộ theo mét.
3. Tạo nhiều mức cao với độ thu nhỏ dần để thể hiện phân tầng khối.
4. Triangulate mặt đáy và mặt mái, rồi nối các lớp bằng các mặt bên.
5. Xuất mesh sang glTF và xuất footprint theo tầng sang GeoJSON để kiểm tra.
