# Báo cáo cá nhân — NguyenNamKhanh-2A202603871

## 1. Thông tin thành viên

- Họ tên: Nguyễn Nam Khánh
- MSSV: 2A202603871
- Email: 26ai.khanhnn3@vinuni.edu.vn
- Vai trong nhóm: Người kiểm số

## 2. Phần việc phụ trách

- CP1: Kiểm độc lập một khoản chi phí trong bảng A2.
- CP4: Tính và đối chiếu năm câu D1, tỷ lệ mở lại và thời gian gom mẫu.
- CP5: Tổng hợp báo cáo nhóm, điền phiếu NHKT chấm TLiet và cập nhật phản hồi duyệt chéo.

## 3. Đóng góp cụ thể

- **CP1:** Cộng 890 phút từ cột `phut_xem_lai_simulated` trong CSV, nhân 2.000 đ/phút và đối chiếu **1.780.000 đ** (simulated) với dòng Xem lại của A2.
- **CP4:** Bổ sung code tính năm câu D1. Với 20 nhân viên mỗi nhóm và mục tiêu phát hiện chênh lệch 6 điểm phần trăm, cần 299 ca/người (5.980 ca thực tế mỗi nhóm). Kiểm tỷ lệ mở lại **39/982 = 3,97%** trong hai loại thuộc phạm vi pilot. Từ lưu lượng giả định và tỷ trọng 982/1.200, ước tính khoảng 10 ngày gom mẫu và 7 ngày theo dõi kể từ ca cuối.
- **CP5:** Ghi phiếu NHKT chấm TLiet **30/30**, kèm câu hỏi về CPS của `hang_nang` và câu trả lời dự kiến. Tổng hợp phản hồi của Nhóm 101 trong báo cáo nhóm. Cập nhật luật dừng để dùng ngưỡng 6.000 đ/việc cho chi phí biến đổi và so chênh 2 điểm phần trăm tỷ lệ mở lại từ bước 10 nhân viên.

## 4. Bằng chứng

- `bd18f66` · Đối chiếu khoản Xem lại. [Bảng A2](bang_chi_phi.md#L13)
- `84ef905` · Phép tính và kết quả D1. [Code](../../src/lab13.py) · [Kế hoạch pilot](pilot_plan.yaml)
- `bdf9d69`, `60c5dae` · Hồ sơ CP5 và cập nhật phản hồi nhận được. [Báo cáo nhóm](group_report.md) · [Phiếu NHKT chấm TLiet](phieu_cham.md)

## 5. Công cụ AI đã dùng

Dùng Codex để hỗ trợ viết và chạy code D1, đối chiếu số liệu và soạn nội dung bàn giao. Kiểm kết quả A2 bằng cách cộng cột phút trong CSV rồi nhân đơn giá. So đầu ra D1 của `lab13.py` với công thức và số đối chiếu trong hướng dẫn lab.

## 6. Tự đánh giá

Tôi đối chiếu được khoản xem lại từ dữ liệu gốc và bàn giao được cỡ mẫu, tỷ lệ mở lại cùng giả định thời gian gom mẫu. Khi chạy pilot, cần kiểm số ca đủ điều kiện theo từng nhân viên ở cả hai nhóm và chờ đủ 7 ngày theo dõi ca cuối trước khi đọc chỉ số chính.
