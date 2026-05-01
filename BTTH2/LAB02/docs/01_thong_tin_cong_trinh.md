# Thông tin công trình: Nhà hát Thành phố Hồ Chí Minh

## 1. Thông tin chung

- **Tên công trình:** Nhà hát Thành phố Hồ Chí Minh
- **Tên gọi khác:** Nhà hát Lớn Sài Gòn, Saigon Opera House, Municipal Theatre of Ho Chi Minh City
- **Địa chỉ:** Số 7 Công trường Lam Sơn, Quận 1, Thành phố Hồ Chí Minh
- **Tọa độ nhóm chọn:**
  - Vĩ độ: `10.776783598907993`
  - Kinh độ: `106.70317240490061`
  - Thứ tự tọa độ dùng trong GeoJSON: `[106.70317240490061, 10.776783598907993]`
- **Loại công trình:** Công trình kiến trúc - văn hóa - biểu diễn nghệ thuật
- **Chức năng hiện nay:** Địa điểm tổ chức các chương trình âm nhạc, sân khấu, nghệ thuật truyền thống, giao hưởng và các sự kiện lớn.

## 2. Lịch sử hình thành

Nhà hát Thành phố Hồ Chí Minh được xây dựng trong giai đoạn **1898 - 1900** dưới thời Pháp thuộc. Đây là một trong những công trình văn hóa tiêu biểu của Sài Gòn cũ, được đầu tư lớn và có vị trí nổi bật ở khu trung tâm đô thị.

Trong lịch sử sử dụng, công trình từng bị hư hỏng vào năm 1944, sau đó được sửa chữa. Năm 1955, nhà hát được cải tạo để làm trụ sở Quốc hội, sau là Hạ nghị viện của chính quyền Việt Nam Cộng hòa. Sau ngày 30/4/1975, công trình trở lại chức năng biểu diễn nghệ thuật.

Năm 1998, nhân dịp kỷ niệm 300 năm hình thành Thành phố Hồ Chí Minh, mặt tiền nhà hát được trùng tu, phục hồi theo thiết kế ban đầu. Giai đoạn 2007 - 2009, công trình tiếp tục được tân trang một số hạng mục kiến trúc và nâng cấp hệ thống ghế ngồi, ánh sáng, âm thanh.

Ngày **29/03/2012**, Nhà hát Thành phố Hồ Chí Minh được công nhận là **Di tích kiến trúc nghệ thuật cấp quốc gia**.

## 3. Đặc điểm kiến trúc

Công trình mang dấu ấn kiến trúc Pháp cuối thế kỷ XIX. Theo Cơ sở dữ liệu ngành Du lịch Việt Nam, nhà hát được xây dựng theo phong cách **Gothic flamboyant**, với nhiều hoa văn, phù điêu và chi tiết trang trí lấy cảm hứng từ các công trình nghệ thuật, nhà hát ở Paris.

Một số đặc điểm nên thể hiện khi dựng mô hình 3D:

- Mặt đứng trước có bố cục đối xứng, nhiều chi tiết trang trí.
- Khối nhà chính có dạng nhà hát cổ điển, gồm tầng trệt và các tầng lầu.
- Phần mái có độ dốc và màu sắc nổi bật so với thân nhà.
- Mặt tiền có các cửa lớn, cửa vòm, cột/trụ trang trí và phù điêu.
- Hai bên công trình có các khối phụ theo trục dọc của nhà hát.
- Màu sắc nên ưu tiên gam vàng/kem cho tường, đỏ/nâu cho mái, và màu tối hơn cho cửa, cửa sổ, chi tiết bóng đổ.

## 4. Gợi ý dữ liệu cho bài lab ArcGIS JS

Để phù hợp yêu cầu **LoD 3**, mô hình không nên chỉ là một khối hộp đơn giản. Nên chia công trình thành nhiều thành phần riêng:

| Thành phần | Cách biểu diễn gợi ý |
| --- | --- |
| Khối thân chính | Polygon footprint + extrusion theo chiều cao ước lượng |
| Sảnh/mặt tiền trước | Khối nhỏ nhô ra phía Công trường Lam Sơn |
| Mái chính | Khối mái dốc hoặc các polygon riêng có vật liệu màu đỏ/nâu |
| Cửa lớn mặt tiền | Các mặt phẳng/mesh trang trí màu tối hoặc kính |
| Cửa sổ | Các đối tượng nhỏ lặp lại trên mặt đứng |
| Cột/trụ trang trí | Các khối hình trụ/hộp nhỏ đặt ở mặt tiền |
| Chi tiết phù điêu | Có thể biểu diễn bằng các khối/phiến trang trí đơn giản nếu không dùng texture |

## 5. Tọa độ tham chiếu

```json
{
  "name": "Nhà hát Thành phố Hồ Chí Minh",
  "latitude": 10.776783598907993,
  "longitude": 106.70317240490061,
  "geojson_position": [106.70317240490061, 10.776783598907993]
}
```

## 6. Nguồn tham khảo

- Cơ sở dữ liệu ngành Du lịch Việt Nam - Nhà hát Thành phố Hồ Chí Minh: https://csdl.vietnamtourism.gov.vn/dest/?item=381
- Đề bài Lab 02: `BTTH/BTTH2/lab02_de_bai.docx`
