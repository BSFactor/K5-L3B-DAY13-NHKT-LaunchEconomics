# Báo cáo cá nhân - Nguyễn Văn Hùng · NHKT · L3B

## 1. Thông tin thành viên

- Họ tên: Nguyễn Văn Hùng
- MSSV: 2A202603816
- Email: 26ai.hungnv12@vinuni.edu.vn
- Vai trong nhóm: Người gắn nhãn 2, kiêm giữ hồ sơ

## 2. Phần việc phụ trách

- **CP1 - A4:** phụ trách phần chi phí cố định của phạm vi `noi_dia` + `hang_nang`: kiểm tra cách phân bổ 40.000.000 đ/tháng trên số việc thành công dự kiến, đối chiếu kết quả A4 với mô hình A2 và tổng hợp vào hồ sơ launch.
- **CP2 - B4:** kiểm tra kịch bản nhân viên xem lại 100% gợi ý, viết nhận xét về ảnh hưởng đến CPS và chuẩn bị bằng chứng độ nhạy để đưa vào hồ sơ.
- **CP3 - C:** gắn nhãn độc lập 20 ca lỗi với vai trò Người gắn nhãn 2; sau đó cùng Người gắn nhãn 1 đối chiếu, phân tích các ca bất đồng và thống nhất bảng lỗi, bảng khắc phục.
- **CP5 - E3:** quản lý `report/team/ho_so_launch_v0.md`; cập nhật dần những mục đã có kết quả kiểm chứng, phối hợp nhận bằng chứng D–E và ghi đề xuất Gate 2a sau khi nhóm thống nhất.

## 3. Đóng góp cụ thể

- **A4:** đối chiếu chi phí biến đổi 3.072.513 đ cho 900 việc thành công trong phạm vi; kiểm tra phân bổ chi phí cố định 40.000.000 đ/tháng. Theo giả định quy mô của bài, CPS sau chi phí cố định đạt **4.599 đ/việc** ở 45.000 yêu cầu/tháng và **5.784 đ/việc** ở 22.500 yêu cầu/tháng (**simulated**). Phần code tính toán do nhóm triển khai; không nhận là người viết code A4.
- **B4:** kiểm tra kịch bản xem lại 100%: CPS **11.743 đ/việc thành công** khi giả định 9 phút làm lại; kịch bản 15,3 phút làm lại cho CPS **12.414 đ** (đều **simulated**). Nhận xét: việc xem lại toàn bộ gợi ý có thể làm mất lợi thế kinh tế, nên pilot phải đo thời gian xem lại và làm lại. Không nhận là người viết code B4.
- **C:** gắn nhãn độc lập 20 ca theo phần việc được giao; phối hợp **Nguyễn Trọng Nghĩa** đối chiếu hai bộ nhãn và chuẩn hóa `bang_loi.md`. Kết quả chung: **16/20 ca trùng (80%)**; bốn ca bất đồng **7, 8, 10, 13** đã có quy tắc phân biệt và nhãn thống nhất; bảng khắc phục chọn đủ năm loại lỗi.
- **Hồ sơ launch:** điền thông tin nhóm NHKT, lớp L3B; tổng hợp bằng chứng A2, B1/B2, A4 và C ở các mục tương ứng. Đã chuẩn bị số liệu rủi ro từ B1/B4 để cập nhật E3, nhưng **không coi E2 là hoàn tất** khi `chi_so.md` chưa có bảng rủi ro được nhóm xác nhận. Chưa chốt mục chỉ số, kế hoạch pilot hoặc quyết định Go/No-go nếu thiếu bằng chứng D–E.

## 4. Bằng chứng

- `report/team/bang_chi_phi.md`: các kết quả A4, B4 và dữ liệu B1 dùng để phân tích rủi ro.
- `src/lab13.py`: chương trình tính toán của nhóm, dùng để đối chiếu số liệu; không phải bằng chứng tôi trực tiếp viết code.
- `report/team/bang_loi.md`: cột Người gắn nhãn 2, hai bộ nhãn độc lập, tỉ lệ đồng thuận 80%, bốn ca bất đồng và bảng khắc phục đủ năm loại.
- `report/team/ho_so_launch_v0.md`: các mục đã cập nhật dựa trên bằng chứng A–C; những nội dung đang chờ D–E giữ trạng thái chưa hoàn thành.
- Commit/PR do bản thân thực hiện: **[BỔ SUNG LINK PR HOẶC MÃ COMMIT SAU KHI XÁC NHẬN TRÊN GITHUB]**.

## 5. Công cụ AI đã dùng

- **ChatGPT:** hỗ trợ giải thích CPS và cách phân bổ chi phí cố định; đối chiếu yêu cầu A4, B4, CP3 và E3 với tài liệu lab; hỗ trợ kiểm tra số liệu, rà soát cách diễn đạt trong hồ sơ và báo cáo cá nhân.
- **Cách tự kiểm tra:** chạy hoặc đối chiếu kết quả `src/lab13.py` với `bang_chi_phi.md`; kiểm tra `bang_loi.md` có đủ 20 ca mỗi người, 16 ca trùng, bốn ca bất đồng có quy tắc phân biệt và năm cách khắc phục có thể đo lường. Nhãn độc lập và nhãn thống nhất được ghi theo kết quả do nhóm thực hiện, không lấy nhãn do AI tự tạo làm kết quả chính thức.

## 6. Tự đánh giá

- **Đã thực hiện:** kiểm tra và tổng hợp A4, B4; tham gia gắn nhãn độc lập, đối chiếu và chuẩn hóa C; cập nhật các mục có bằng chứng trong hồ sơ launch.
- **Cần hoàn tất:**  link commit/PR cá nhân; phối hợp nhận `pilot_plan.yaml` và `chi_so.md` đã được nhóm kiểm tra để hoàn thiện các mục còn thiếu và đề xuất cuối cùng cho Gate 2a.
