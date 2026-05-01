# Cấu Trúc Project LAB02

File quan trọng nhất là `index.html`. Đây là trang demo chính để nộp và trình bày với thầy.

## Sơ Đồ Folder

```text
LAB02/
├── index.html
├── HUONG_DAN.txt
├── README.md
├── data/
│   ├── geojson/
│   │   ├── NhaHatThanhPho_footprint.geojson
│   │   ├── NhaHat_ThanhPho_LoD3.geojson
│   │   └── NhaHat_ThanhPho_LoD3_wgs84.geojson
│   ├── model/
│   │   ├── NhaHat_ThanhPho.gltf
│   │   ├── NhaHat_ThanhPho_LoD3.gltf
│   │   └── reference/
│   │       └── nhahat_reference.glb
│   ├── shapefile/
│   │   ├── NhaHat_Footprint.shp
│   │   ├── NhaHat_Footprint.shx
│   │   ├── NhaHat_Footprint.dbf
│   │   ├── NhaHat_Footprint.prj
│   │   └── NhaHat_Footprint.cpg
│   └── lod3_components.json
├── viewers/
│   ├── geojson_layer_check.html
│   ├── gltf_lod3_check.html
│   └── reference_model.html
├── scripts/
│   └── build_nhathanhpho_lod3.py
├── docs/
│   ├── bao_cao_tom_tat.md
│   ├── phan_cong_LAB2.csv
│   ├── lab02_de_bai.docx
│   ├── 01_thong_tin_cong_trinh.md
│   ├── 05_ghi_chu_dung_3d.md
│   ├── reference_model_note.md
│   └── references/
└── screenshots/
    └── 3d_overview.png
```

## Vai Trò Từng Nhóm File

| Nhóm | Vai trò |
| --- | --- |
| `index.html` | Bài demo chính, dùng ArcGIS SceneView để biểu diễn LoD3 |
| `data/geojson/` | Dữ liệu JSON/GeoJSON theo yêu cầu đề bài |
| `data/shapefile/` | Footprint gốc để chứng minh quy trình xử lý GIS |
| `data/model/` | Model glTF/GLB để kiểm tra hình học 3D |
| `viewers/` | Viewer phụ, không phải phần bắt buộc khi demo |
| `scripts/` | Script Python dựng dữ liệu từ footprint |
| `docs/` | Đề bài, phân công, báo cáo, ghi chú nguồn |
| `screenshots/` | Ảnh kết quả để đưa vào báo cáo nếu cần |

## Nên Demo Theo Thứ Tự

1. Mở `index.html`.
2. Bật/tắt các nhóm LoD3 trong panel.
3. Bật `Footprint GeoJSON` để chứng minh vị trí/footprint.
4. Dùng `Camera 360` để xoay quanh công trình.
5. Nếu thầy hỏi nguồn tham chiếu chi tiết, mở `viewers/reference_model.html`.

## Ghi Chú Tránh Nhầm

- `index.html` là bài chính.
- `viewers/reference_model.html` chỉ là viewer tham chiếu model SketchUp, không thay thế bài chính.
- `data/model/reference/nhahat_reference.glb` khá nặng nên không nên load trực tiếp trong SceneView chính.
- Basemap `dark-gray-vector` vẫn là basemap ArcGIS; project vẫn đáp ứng yêu cầu bản đồ 3D ArcGIS JS.
