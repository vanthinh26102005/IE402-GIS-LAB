# Ghi chú tọa độ và footprint

## 1. Tọa độ trung tâm công trình

Nhóm chọn công trình **Nhà hát Thành phố Hồ Chí Minh** với tọa độ trung tâm tham chiếu:

- Vĩ độ: `10.776783598907993`
- Kinh độ: `106.70317240490061`

Khi dùng trong GeoJSON hoặc ArcGIS JS, cần viết theo thứ tự:

```json
[106.70317240490061, 10.776783598907993]
```

Thứ tự này là `[longitude, latitude]`, tức là `[kinh độ, vĩ độ]`.

## 2. Hướng công trình

Mặt trước của Nhà hát Thành phố Hồ Chí Minh hướng ra khu vực **Công trường Lam Sơn**. Khi dựng mô hình 3D, nên xác định hướng mặt tiền trước để đặt các chi tiết như:

- Sảnh chính
- Cột/trụ trang trí
- Cửa lớn mặt tiền
- Các chi tiết phù điêu hoặc trang trí nổi bật

Ảnh `orientation_reference.png` dùng để ghi chú hướng nhìn, hướng mặt tiền và hướng các mặt bên của công trình.

## 3. Footprint tham chiếu

Footprint là đường bao mặt bằng công trình nhìn từ trên xuống. Trong bài lab, footprint có thể được dùng để:

- Xác định vị trí đặt mô hình trên bản đồ.
- Tạo khối thân chính bằng polygon.
- Chia công trình thành các khối phụ: thân chính, sảnh trước, hai khối bên, phần mái.
- Canh tỉ lệ tương đối giữa chiều dài, chiều rộng và hướng xoay của mô hình.

Ảnh `footprint_reference.png` dùng để lưu ảnh chụp bản đồ hoặc sơ đồ mặt bằng tham chiếu. Khi có ảnh thật, nên đánh dấu:

- Đường bao công trình
- Hướng Bắc
- Mặt trước công trình
- Tọa độ trung tâm
- Các khối chính cần dựng trong mô hình 3D

## 4. Gợi ý cấu trúc tọa độ khi tạo GeoJSON

Ví dụ một điểm trung tâm công trình:

```json
{
  "type": "Feature",
  "properties": {
    "name": "Nhà hát Thành phố Hồ Chí Minh",
    "type": "landmark",
    "lod": 3
  },
  "geometry": {
    "type": "Point",
    "coordinates": [106.70317240490061, 10.776783598907993]
  }
}
```

Khi dựng footprint dạng polygon, điểm đầu và điểm cuối của vòng tọa độ phải trùng nhau để đóng kín polygon.

