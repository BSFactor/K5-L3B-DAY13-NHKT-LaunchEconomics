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

### Đóng góp cụ thể

- Gắn độc lập cột "Nhãn người 1" cho 20 ca; so với Người gắn nhãn 2: 4 ca không trùng (7, 8, 10, 13), đồng thuận 16/20 = 80%.
- Viết quy tắc phân biệt cho 4 ca không trùng và bảng khắc phục 5 ca, mỗi loại một ca (6, 20, 10, 19, 12), mỗi dòng có ngưỡng đo được và một vai trò phụ trách.
- Điền pilot_plan.yaml: chia theo nhân viên 20 + 20, chấp nhận mức chênh 6 điểm (859 ca hiệu dụng/nhóm, DE 6,96; power còn khoảng 0,64 nếu tác động thật là 5 điểm); ba luật dừng an toàn, chi phí, mức độ sử dụng.
- Kiểm tra CP1–CP4 theo mục "Tự kiểm tra" trong `CHECKPOINTS.md`.

### Bằng chứng

- Commit `a4ecb5c` (điền nhãn người 1), `e36337d` (bảng lỗi và báo cáo cá nhân).
- File: `report/team/bang_loi.md`, `report/team/pilot_plan.yaml`, `report/team/2A202603835_NguyenTrongNghia.md`.
- `pilot_plan.yaml` đọc được bằng `yaml.safe_load` và không còn `?` ngoài dòng chú thích.
