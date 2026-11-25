# Báo cáo cá nhân — NguyenTrongNghia-2A202603835

## 1. Thông tin thành viên

- Họ tên: Nguyễn Trọng Nghĩa
- MSSV: 2A202603835
- Email: nghiatrongnguyen2304@gmail.com
- Vai trong nhóm: Người gắn nhãn 1

## 2. Phần việc phụ trách

- Đọc đề, theo dõi điều kiện "Xong khi" / "Tự kiểm tra" của từng checkpoint trong `CHECKPOINTS.md`.
- Nhiệm vụ C (CP3): gắn nhãn độc lập 20 ca lỗi theo năm loại của Google PAIR, so nhãn với Người gắn nhãn 2, hoàn thiện `report/team/bang_loi.md`.
- Nhiệm vụ D (CP4): điền `report/team/pilot_plan.yaml`.
- Nhiệm vụ E (CP5): điền `report/team/chi_so.md` (E1, E2) và các mục 4, 6, 7 cùng dòng đề xuất trong `report/team/ho_so_launch_v0.md`.

## 3. Đóng góp cụ thể

- CP3:
  - Gắn độc lập cột "Nhãn người 1" cho 20 ca, không trao đổi với Người gắn nhãn 2 trước khi so.
  - So nhãn với Nguyễn Văn Hùng: 4 ca không trùng (7, 8, 10, 13), tỉ lệ đồng thuận 16/20 = 80%, đạt ngưỡng nên không phải viết lại định nghĩa.
  - Cùng nhóm thống nhất nhãn cho các ca không trùng và viết một câu quy tắc phân biệt cho mỗi ca; rà lại ca 5 (cả hai cùng gắn "Hệ thống") để nhãn thống nhất khớp với hai bộ nhãn.
  - Hoàn thiện bảng khắc phục 5 ca, mỗi loại một ca (ca 6, 20, 10, 19, 12), mỗi dòng có cách phát hiện đo được (event/đối soát, ngưỡng, tần suất) và một vai trò phụ trách.
- CP4 (`pilot_plan.yaml`):
  - Chọn chia theo nhân viên 20 + 20, ngẫu nhiên phân tầng theo depot, phạm vi noi_dia + hang_nang.
  - Ghi đánh đổi: chấp nhận mức chênh 6 điểm (859 ca hiệu dụng/nhóm, DE 6,96, ít nhất 299 yêu cầu/người); power chỉ còn 0,64 nếu tác động thật là 5 điểm.
  - Trả lời năm câu D2; viết ba luật dừng (an toàn, chi phí, mức độ sử dụng) theo mẫu NẾU – TRONG – THÌ – KHÔNG THÌ, dựa trên tỉ lệ mở lại hiện tại 3,97% và tỉ lệ bỏ qua gợi ý 21,1% trong phạm vi.
- CP5:
  - `chi_so.md`: tính thử ba chỉ số (chính 82,83%, bỏ qua gợi ý 27,12%, mở lại 7 ngày 4,25%), đề xuất thêm hai chỉ số, liệt kê 10 event có `trace_id` và kiểm tra chéo; ba dòng rủi ro kinh tế lấy số từ B1, B4, A4.
  - `ho_so_launch_v0.md`: điền mục 4 (chỉ số), mục 6 (pilot plan), cập nhật mục 7; ghi đề xuất "Go có điều kiện" theo quyết định của nhóm, kèm bốn điều kiện, người phụ trách và ngày kiểm tra.
- Kiểm tra CP1–CP4 theo mục "Tự kiểm tra": chạy `lab13.py`, đối chiếu số trong `bang_chi_phi.md` với output.

## 4. Bằng chứng

- File: `report/team/bang_loi.md`, `report/team/pilot_plan.yaml`, `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md` (mục 4, 6, 7 và dòng đề xuất).
- Commit: `a4ecb5c` (điền nhãn người 1), `e36337d` (bảng lỗi, báo cáo cá nhân), `b4c6827` (pilot_plan.yaml, TEAM.md), và commit cập nhật chỉ số, hồ sơ launch.
- Con số: đồng thuận 16/20 = 80%; 859 ca hiệu dụng/nhóm, DE 6,96, power 0,64; chỉ số chính trong đợt chạy thử 82,83% (994/1.200).
- `pilot_plan.yaml` đọc được bằng `yaml.safe_load` và không còn `?` ngoài dòng chú thích; `chi_so.md` và `ho_so_launch_v0.md` không có từ "production".

## 5. Công cụ AI đã dùng

- Claude Code:
  - Đọc và tóm tắt repo, đọc mô tả 20 ca trong file docx, đối chiếu cột "Trùng?" với hai bộ nhãn, phát hiện chỗ không nhất quán (ca 5; phần quy tắc và bảng khắc phục còn chép từ bài mẫu).
  - Đọc lại mô tả 20 ca, đếm lại số ca không trùng, kiểm tra mỗi dòng khắc phục khớp với nhãn thống nhất.
  - Đối chiếu mọi con số với output `python lab13.py` và với số tham khảo trong hướng dẫn (lệch không quá 2%).
  - Chạy `yaml.safe_load`, lệnh grep tìm `?` và grep "production"

## 6. Tự đánh giá

- Làm được: gắn nhãn độc lập, đạt đồng thuận 80%; pilot plan có đánh đổi ghi rõ bằng số; chỉ số và event đủ để đo cả năm chỉ số.
- Cần cải thiện: ca 8 còn tranh luận giữa "Ngầm" và "Hệ thống"; các ngưỡng cảnh báo và luật dừng (6.000 đ, 40%, 8%) là đề xuất, chưa kiểm chứng bằng dữ liệu thật; phần lớn câu chữ CP4–CP5 do AI soạn nên tôi cần tự giải thích được từng con số khi hội đồng hỏi.
