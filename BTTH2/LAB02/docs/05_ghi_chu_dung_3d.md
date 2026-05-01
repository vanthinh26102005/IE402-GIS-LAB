# Ghi chú dựng mô hình 3D LoD 3

## 1. Mục tiêu dựng mô hình

Bài lab yêu cầu biểu diễn công trình ở mức **LoD 3**. Với Nhà hát Thành phố Hồ Chí Minh, mô hình cần thể hiện được hình khối chính và các đặc trưng kiến trúc dễ nhận biết, không chỉ là một khối hộp đơn giản.

## 2. Các thành phần nên dựng

| Nhóm chi tiết | Nội dung cần thể hiện | Mức ưu tiên |
| --- | --- | --- |
| Khối thân chính | Hình khối lớn của nhà hát, chiều dài, chiều rộng, chiều cao tương đối | Cao |
| Mặt tiền trước | Sảnh chính, cửa lớn, cột/trụ, bố cục đối xứng | Cao |
| Mái nhà | Mái dốc, màu đỏ/nâu, phần mái chính và các mái phụ | Cao |
| Cửa sổ/cửa đi | Các chi tiết lặp lại trên mặt đứng | Trung bình |
| Khối bên trái/phải | Các phần nhô hoặc khối phụ hai bên công trình | Trung bình |
| Chi tiết trang trí | Phù điêu, viền, gờ, hoa văn có thể biểu diễn đơn giản | Thấp đến trung bình |

## 3. Phân rã mô hình đề xuất

Nên chia mô hình thành các lớp hoặc nhóm đối tượng sau:

1. **base_body**: khối thân chính của nhà hát.
2. **front_hall**: phần sảnh hoặc khối nhô ở mặt tiền.
3. **main_roof**: mái chính.
4. **side_roofs**: các mái phụ hai bên.
5. **doors**: cửa chính và cửa phụ.
6. **windows**: các cửa sổ lặp lại.
7. **columns**: cột/trụ trang trí ở mặt tiền.
8. **decorations**: chi tiết trang trí bổ sung nếu còn thời gian.

## 4. Gợi ý màu sắc và vật liệu

- Tường chính: vàng nhạt, kem hoặc be sáng.
- Mái: đỏ gạch, nâu đỏ hoặc đỏ sẫm.
- Cửa và cửa sổ: xanh đậm, nâu đậm, đen hoặc màu kính tối.
- Chi tiết viền/gờ: màu sáng hơn hoặc tối hơn nhẹ so với tường để tạo độ nổi.
- Bóng đổ và cạnh phụ: dùng màu tối hơn để tăng cảm giác chiều sâu.

## 5. Gợi ý triển khai trong ArcGIS JS

Có thể triển khai theo một trong hai hướng:

- **Dữ liệu GeoJSON/JSON + render bằng ArcGIS JS:** lưu footprint, chiều cao và thông tin từng khối vào file dữ liệu, sau đó đọc vào `SceneView`.
- **Dựng trực tiếp bằng Mesh/Graphic:** tạo các khối 3D bằng JavaScript, phù hợp nếu cần nhiều chi tiết hình học.

Các thuộc tính nên có trong dữ liệu:

```json
{
  "id": "base_body",
  "name": "Khối thân chính",
  "height": 22,
  "base_height": 0,
  "color": "#f2d49b",
  "part_type": "body"
}
```

## 6. Kiểm tra trước khi nộp

- Mô hình đặt đúng vị trí Nhà hát Thành phố Hồ Chí Minh.
- Thứ tự tọa độ đúng chuẩn `[kinh độ, vĩ độ]`.
- Có ít nhất các khối chính: thân nhà, mặt tiền, mái, cửa/cửa sổ.
- Mô hình nhìn được rõ trong `SceneView`.
- File nộp gồm HTML và dữ liệu JSON/GeoJSON, hoặc repo GitHub có đầy đủ mã nguồn.

