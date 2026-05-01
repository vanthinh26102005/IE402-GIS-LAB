# Báo cáo tóm tắt Lab 02

## Công trình

- Tên: Nhà hát Thành phố Hồ Chí Minh.
- Vị trí: số 7 Công trường Lam Sơn, Quận 1, Thành phố Hồ Chí Minh.
- Tọa độ dùng trong bài: `[106.70317240490061, 10.776783598907993]`.
- Mức biểu diễn: LoD3 theo phạm vi bài thực hành, không phải mô hình BIM đo đạc.

## Quy trình dữ liệu

1. Thu thập thông tin công trình, ảnh mặt đứng, ảnh mái, ảnh chi tiết kiến trúc và ghi chú nguồn.
2. Số hóa footprint ban đầu dưới dạng GeoJSON.
3. Chuẩn hóa footprint sang shapefile và GeoJSON WGS84.
4. Dựng khối tầng bằng extrusion, xuất thêm glTF để kiểm tra hình học.
5. Bổ sung chi tiết LoD3 trong SceneView: khối chính, khối phụ, mái, cửa, cửa sổ, ban công, gờ nổi và chi tiết mặt đứng.
6. Đóng gói viewer, dữ liệu, script, tài liệu và hướng dẫn chạy vào `BTTH2/LAB02`.

## Kết quả

| Hạng mục | File |
| --- | --- |
| Viewer LoD3 chính | `index.html` |
| Viewer GeoJSON phụ | `viewers/geojson_layer_check.html` |
| Viewer glTF phụ | `viewers/gltf_lod3_check.html` |
| Viewer model tham chiếu | `viewers/reference_model.html` |
| Footprint GeoJSON | `data/geojson/NhaHatThanhPho_footprint.geojson` |
| GeoJSON tầng khối | `data/geojson/NhaHat_ThanhPho_LoD3_wgs84.geojson` |
| Metadata lớp LoD3 | `data/lod3_components.json` |
| Mô hình glTF | `data/model/NhaHat_ThanhPho_LoD3.gltf` |
| Model tham chiếu GLB | `data/model/reference/nhahat_reference.glb` |
| Shapefile footprint | `data/shapefile/NhaHat_Footprint.shp` |

## Ghi chú nghiệm thu

- Mô hình chính không chỉ là một khối extrusion đơn giản; các nhóm chi tiết được tách thành nhiều lớp có thể bật/tắt.
- Có popup cho từng khối trong SceneView.
- Có footprint GeoJSON tham chiếu có thể bật/tắt trong viewer chính.
- Các file nộp có thể chạy bằng local server theo `HUONG_DAN.txt`.
