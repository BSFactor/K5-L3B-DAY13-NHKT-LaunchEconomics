# Team

## Thông tin nhóm

- Tên nhóm: NHKT
- Lớp: L3B
- Repo nhóm: [K5-L3B-DAY13-NHKT-LaunchEconomics](https://github.com/BSFactor/K5-L3B-DAY13-NHKT-LaunchEconomics)
- Nhánh hồ sơ để nộp: [`main`](https://github.com/BSFactor/K5-L3B-DAY13-NHKT-LaunchEconomics/tree/main)
- Commit chốt nội dung CP5 đã push: [`bdf9d69`](https://github.com/BSFactor/K5-L3B-DAY13-NHKT-LaunchEconomics/commit/bdf9d69)

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 |   Nguyễn Trọng Nghĩa     |   2A202603835   |   nghiatrongnguyen2304@gmail.com    |   trongnghia2304     |   Người gắn nhãn 1      |
|   2 |    Nguyễn Văn Hùng    |   2A202603816   |    26ai.hungnv12@vinuni.edu.vn   |    nguyenhung1901    |    Người gắn nhãn 2 kiêm giữ hồ sơ     |
|   3 |    Nguyễn Minh Thành    |   2A202603884   |   26ai.thanhnm@vinuni.edu.vn    |   thanhhy98     |   Người viết code      |
|   4 |    Nguyễn Nam Khánh    |   2A202603871   |   26ai.khanhnn3@vinuni.edu.vn    |   BSFactor     |     Người kiểm số    |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Đóng góp của từng thành viên

## NguyenTrongNghia-2A202603835

### Phần việc phụ trách

- Người gắn nhãn 1: đọc đề, theo dõi điều kiện "Xong khi" / "Tự kiểm tra" của từng checkpoint.
- CP3: gắn nhãn độc lập 20 ca lỗi, so nhãn, hoàn thiện `report/team/bang_loi.md`.
- CP4: điền `report/team/pilot_plan.yaml` (D2, đánh đổi, luật dừng, các trường còn `?`).
- CP5: điền `report/team/chi_so.md` (E1, E2) và mục 4, 6, 7 cùng dòng đề xuất trong `report/team/ho_so_launch_v0.md`.

### Đóng góp cụ thể

- Gắn độc lập cột "Nhãn người 1" cho 20 ca; so với Người gắn nhãn 2: 4 ca không trùng (7, 8, 10, 13), đồng thuận 16/20 = 80%.
- Viết quy tắc phân biệt cho 4 ca không trùng và bảng khắc phục 5 ca, mỗi loại một ca (6, 20, 10, 19, 12), mỗi dòng có ngưỡng đo được và một vai trò phụ trách.
- Điền pilot_plan.yaml: chia theo nhân viên 20 + 20, chấp nhận mức chênh 6 điểm (859 ca hiệu dụng/nhóm, DE 6,96; power còn khoảng 0,64 nếu tác động thật là 5 điểm); bốn luật dừng (hai luật an toàn: hoàn trùng dừng ngay, mở lại đánh giá theo tuần; chi phí; mức độ sử dụng); ghi chú hiệu chỉnh baseline cho phạm vi pilot.
- E1: tính thử ba chỉ số (chính 82,83%, bỏ qua gợi ý 27,12%, mở lại 7 ngày 4,25%), đề xuất thêm hai chỉ số, 10 event có `trace_id` và kiểm tra chéo; E2: ba dòng rủi ro kinh tế lấy số từ B1, B4, A4.
- Hồ sơ launch: điền mục 4, 6, cập nhật mục 7 và ghi đề xuất "Go có điều kiện" (quyết định của nhóm) với bốn điều kiện, người phụ trách và ngày kiểm tra.
- Kiểm tra CP1–CP4 theo mục "Tự kiểm tra" trong `CHECKPOINTS.md`.

### Bằng chứng

- Commit `a4ecb5c` (điền nhãn người 1), `e36337d` (bảng lỗi và báo cáo cá nhân), `b4c6827` (pilot_plan.yaml, TEAM.md), và `f7f269b` (chỉ số và hồ sơ launch).
- [Bảng lỗi](report/team/bang_loi.md) · [Kế hoạch pilot](report/team/pilot_plan.yaml) · [Bảng chỉ số](report/team/chi_so.md) · [Hồ sơ launch](report/team/ho_so_launch_v0.md) · [Báo cáo cá nhân](report/team/2A202603835_NguyenTrongNghia.md)
- `pilot_plan.yaml` đọc được bằng `yaml.safe_load` và không còn `?` ngoài dòng chú thích; `chi_so.md` và `ho_so_launch_v0.md` không có từ "production".

## NguyenVanHung-2A202603816

### Phần việc phụ trách

- Người gắn nhãn 2, kiêm giữ hồ sơ: kiểm tra A4, nhận xét B4, gắn nhãn độc lập 20 ca CP3 và tổng hợp bằng chứng vào `ho_so_launch_v0.md`.

### Đóng góp cụ thể

- A4: đối chiếu phân bổ chi phí cố định 40 triệu đ/tháng, CPS 4.599/5.784 đ theo hai mức tải (simulated). B4: kiểm tra CPS 11.743 đ khi xem lại 100%, tăng lên 12.414 đ nếu làm lại mất 15,3 phút (simulated). CP3: gắn nhãn người 2, cùng Nguyễn Trọng Nghĩa đối chiếu 20 ca (16/20 trùng, 80%), thống nhất bốn ca bất đồng. E3: cập nhật bằng chứng A–C; rà hồ sơ cuối theo kết quả D–E của nhóm.

### Bằng chứng

- Commit `2cc3f57` (nhãn người 2); `6787181`, `c7aebaa`, `81f3f4c`, `d08b1cc` (các lần cập nhật hồ sơ và báo cáo cá nhân). [Bảng lỗi](report/team/bang_loi.md) · [Hồ sơ launch](report/team/ho_so_launch_v0.md) · [Báo cáo cá nhân](report/team/2A202603816_NguyenVanHung.md)

## NguyenMinhThanh-2A202603884

### Phần việc phụ trách

- Viết và chạy `src/lab13.py`, đối chiếu đầu ra và giải thích các giả định tính toán.

### Đóng góp cụ thể

- Triển khai ba phép thử A1, mô hình chi phí A2, phân nhóm A3, phí cố định A4 và kịch bản độ nhạy B1–B4. Đối chiếu đầu ra với bảng chi phí, gồm 978 việc thành công và CPS khoảng 4.472 đ/việc (simulated).

### Bằng chứng

- Commit `8cae1c5` và `cbefae2`. [Code](src/lab13.py) · [Bảng chi phí](report/team/bang_chi_phi.md) · [Báo cáo cá nhân](report/team/2A202603884_NguyenMinhThanh.md)

## NguyenNamKhanh-2A202603871

### Phần việc phụ trách

- Kiểm số CP1, tiếp quản phép tính D1 ở CP4 và tổng hợp bản bàn giao CP5.

### Đóng góp cụ thể

- Kiểm khoản xem lại từ CSV, 890 phút × 2.000 đ = 1.780.000 đ (simulated). Viết và đối chiếu năm phép tính D1, kiểm tỷ lệ mở lại 39/982 = 3,97% trong phạm vi pilot và ước tính 10 ngày gom mẫu cộng 7 ngày theo dõi. Tổng hợp báo cáo nhóm, ghi phiếu NHKT chấm TLiet 30/30 và cập nhật luật dừng theo góp ý nhận được.

### Bằng chứng

- Commit `bd18f66` (kiểm số CP1), `84ef905` (kiểm số CP4), `bdf9d69` (hồ sơ và duyệt chéo CP5). [Báo cáo cá nhân](report/team/2A202603871_NguyenNamKhanh.md) · [Kế hoạch pilot](report/team/pilot_plan.yaml) · [Phiếu chấm TLiet](report/team/phieu_cham.md)
