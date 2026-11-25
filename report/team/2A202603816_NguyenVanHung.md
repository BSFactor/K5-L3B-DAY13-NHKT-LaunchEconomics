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
- **CP5 - E3:** giữ `report/team/ho_so_launch_v0.md`, tổng hợp bằng chứng A–C; đối chiếu hồ sơ hoàn chỉnh với kết quả D–E và đề xuất Gate 2a do nhóm thống nhất.

## 3. Đóng góp cụ thể

- **A4:** đối chiếu chi phí biến đổi 3.072.513 đ cho 900 việc thành công trong phạm vi; kiểm tra phân bổ chi phí cố định 40.000.000 đ/tháng. Theo giả định quy mô của bài, CPS sau chi phí cố định đạt **4.599 đ/việc** ở 45.000 yêu cầu/tháng và **5.784 đ/việc** ở 22.500 yêu cầu/tháng (**simulated**). Phần code tính toán do nhóm triển khai; không nhận là người viết code A4.
- **B4:** kiểm tra kịch bản xem lại 100%: CPS **11.743 đ/việc thành công** khi giả định 9 phút làm lại; kịch bản 15,3 phút làm lại cho CPS **12.414 đ** (đều **simulated**). Nhận xét: việc xem lại toàn bộ gợi ý có thể làm mất lợi thế kinh tế, nên pilot phải đo thời gian xem lại và làm lại. Không nhận là người viết code B4.
- **C:** gắn nhãn độc lập 20 ca theo phần việc được giao; phối hợp **Nguyễn Trọng Nghĩa** đối chiếu hai bộ nhãn và chuẩn hóa `bang_loi.md`. Kết quả chung: **16/20 ca trùng (80%)**; bốn ca bất đồng **7, 8, 10, 13** đã có quy tắc phân biệt và nhãn thống nhất; bảng khắc phục chọn đủ năm loại lỗi.
- **Hồ sơ launch:** cập nhật thông tin NHKT, L3B và bằng chứng A–C trong `ho_so_launch_v0.md`, gồm các số liệu A4/B4 và kết quả gắn nhãn. Bản `main` hiện đã có đầy đủ bảy mục và đề xuất **Go có điều kiện**; phần pilot D, chỉ số E1–E2 và các cập nhật mục 4, 6, 7 do thành viên khác phụ trách. Tôi giữ vai trò tổng hợp/đối chiếu hồ sơ, không nhận các phần đó là đóng góp cá nhân.

## 4. Bằng chứng

- `report/team/bang_chi_phi.md`: các kết quả A4, B4 và dữ liệu B1 dùng để phân tích rủi ro.
- `src/lab13.py`: chương trình tính toán của nhóm, dùng để đối chiếu số liệu; không phải bằng chứng tôi trực tiếp viết code.
- `report/team/bang_loi.md`: cột Người gắn nhãn 2, hai bộ nhãn độc lập, tỉ lệ đồng thuận 80%, bốn ca bất đồng và bảng khắc phục đủ năm loại.
- `report/team/ho_so_launch_v0.md`: bằng chứng kinh tế, bảng lỗi và hồ sơ chốt đủ bảy mục; các mục D–E bổ sung sau là kết quả chung của nhóm.
- **Commit cá nhân trên `main`:** [`2cc3f57`](https://github.com/BSFactor/K5-L3B-DAY13-NHKT-LaunchEconomics/commit/2cc3f57) (nhãn người 2); [`6787181`](https://github.com/BSFactor/K5-L3B-DAY13-NHKT-LaunchEconomics/commit/6787181) (chuẩn bị hồ sơ); [`c7aebaa`](https://github.com/BSFactor/K5-L3B-DAY13-NHKT-LaunchEconomics/commit/c7aebaa) (bằng chứng kinh tế); [`81f3f4c`](https://github.com/BSFactor/K5-L3B-DAY13-NHKT-LaunchEconomics/commit/81f3f4c) (cập nhật hồ sơ); [`d08b1cc`](https://github.com/BSFactor/K5-L3B-DAY13-NHKT-LaunchEconomics/commit/d08b1cc) (hồ sơ và báo cáo cá nhân).

## 5. Công cụ AI đã dùng

- **ChatGPT:** hỗ trợ giải thích CPS và cách phân bổ chi phí cố định; đối chiếu yêu cầu A4, B4, CP3 và E3 với tài liệu lab; hỗ trợ kiểm tra số liệu, rà soát cách diễn đạt trong hồ sơ và báo cáo cá nhân.
- **Cách tự kiểm tra:** chạy hoặc đối chiếu kết quả `src/lab13.py` với `bang_chi_phi.md`; kiểm tra `bang_loi.md` có đủ 20 ca mỗi người, 16 ca trùng, bốn ca bất đồng có quy tắc phân biệt và năm cách khắc phục có thể đo lường. Nhãn độc lập và nhãn thống nhất được ghi theo kết quả do nhóm thực hiện, không lấy nhãn do AI tự tạo làm kết quả chính thức.

## 6. Tự đánh giá

- **Đã thực hiện:** kiểm tra và tổng hợp A4, B4; tham gia gắn nhãn độc lập, đối chiếu và chuẩn hóa C; cập nhật các mục có bằng chứng trong hồ sơ launch.
