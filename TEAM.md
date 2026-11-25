# Team

## Thông tin nhóm

- Tên nhóm:
- Lớp: L3A hoặc L3B
- Repo nhóm: `K5-L3A-DAY13-TenNhom-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt:

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 |   Nguyễn Trọng Nghĩa     |   2A202603835   |   nghiatrongnguyen2304@gmail.com    |   trongnghia2304     |   Người gắn nhãn 1      |
|   2 |    Nguyễn Văn Hùng    |   2A202603816   |    26ai.hungnv12@vinuni.edu.vn   |    nguyenhung1901    |    Người gắn nhãn 2     |
|   3 |    Nguyễn Minh Thành    |   2A202603884   |   26ai.thanhnm@vinuni.edu.vn    |   thanhhy98     |   Người viết code      |
|   4 |    Nguyễn Nam Khánh    |   2A202603871   |   26ai.khanhnn3@vinuni.edu.vn    |   BSFactor     |     Người kiểm số    |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## HoVaTen-MSSV

### Phần việc phụ trách

-

### Đóng góp cụ thể

-

### Bằng chứng

-

## NguyenTrongNghia-2A202603835

### Phần việc phụ trách

- Người gắn nhãn 1: đọc đề, theo dõi điều kiện "Xong khi" / "Tự kiểm tra" của từng checkpoint.
- CP3: gắn nhãn độc lập 20 ca lỗi, so nhãn, hoàn thiện `report/team/bang_loi.md`.
- CP4: điền `report/team/pilot_plan.yaml` (D2, đánh đổi, luật dừng, các trường còn `?`).
- CP5: điền `report/team/chi_so.md` (E1, E2) và mục 4, 6, 7 cùng dòng đề xuất trong `report/team/ho_so_launch_v0.md`.

### Đóng góp cụ thể

- Gắn độc lập cột "Nhãn người 1" cho 20 ca; so với Người gắn nhãn 2: 4 ca không trùng (7, 8, 10, 13), đồng thuận 16/20 = 80%.
- Viết quy tắc phân biệt cho 4 ca không trùng và bảng khắc phục 5 ca, mỗi loại một ca (6, 20, 10, 19, 12), mỗi dòng có ngưỡng đo được và một vai trò phụ trách.
- Điền pilot_plan.yaml: chia theo nhân viên 20 + 20, chấp nhận mức chênh 6 điểm (859 ca hiệu dụng/nhóm, DE 6,96; power còn khoảng 0,64 nếu tác động thật là 5 điểm); ba luật dừng an toàn, chi phí, mức độ sử dụng.
- E1: tính thử ba chỉ số (chính 82,83%, bỏ qua gợi ý 27,12%, mở lại 7 ngày 4,25%), đề xuất thêm hai chỉ số, 10 event có `trace_id` và kiểm tra chéo; E2: ba dòng rủi ro kinh tế lấy số từ B1, B4, A4.
- Hồ sơ launch: điền mục 4, 6, cập nhật mục 7 và ghi đề xuất "Go có điều kiện" (quyết định của nhóm) với bốn điều kiện, người phụ trách và ngày kiểm tra.
- Kiểm tra CP1–CP4 theo mục "Tự kiểm tra" trong `CHECKPOINTS.md`.

### Bằng chứng

- Commit `a4ecb5c` (điền nhãn người 1), `e36337d` (bảng lỗi và báo cáo cá nhân), `b4c6827` (pilot_plan.yaml, TEAM.md), và commit cập nhật chỉ số, hồ sơ launch.
- File: `report/team/bang_loi.md`, `report/team/pilot_plan.yaml`, `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`, `report/team/2A202603835_NguyenTrongNghia.md`.
- `pilot_plan.yaml` đọc được bằng `yaml.safe_load` và không còn `?` ngoài dòng chú thích; `chi_so.md` và `ho_so_launch_v0.md` không có từ "production".
