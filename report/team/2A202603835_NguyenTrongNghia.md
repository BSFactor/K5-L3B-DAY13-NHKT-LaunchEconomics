# Báo cáo cá nhân — NguyenTrongNghia-2A202603835

## 1. Thông tin thành viên

- Họ tên: Nguyễn Trọng Nghĩa
- MSSV: 2A202603835
- Email: nghiatrongnguyen2304@gmail.com
- Vai trong nhóm: Người gắn nhãn 1

## 2. Phần việc phụ trách

- Đọc đề, theo dõi điều kiện "Xong khi" / "Tự kiểm tra" của từng checkpoint trong `CHECKPOINTS.md`.
- Nhiệm vụ C (CP3): gắn nhãn độc lập 20 ca lỗi theo năm loại của Google PAIR, so nhãn với Người gắn nhãn 2, hoàn thiện `report/team/bang_loi.md`.

## 3. Đóng góp cụ thể

- Gắn độc lập cột "Nhãn người 1" cho 20 ca, không trao đổi với Người gắn nhãn 2 trước khi so.
- So nhãn với Nguyễn Văn Hùng: 4 ca không trùng (7, 8, 10, 13), tỉ lệ đồng thuận 16/20 = 80%, đạt ngưỡng nên không phải viết lại định nghĩa.
- Cùng nhóm thống nhất nhãn cho các ca không trùng và viết một câu quy tắc phân biệt cho mỗi ca; rà lại ca 5 (cả hai cùng gắn "Hệ thống") để nhãn thống nhất khớp với hai bộ nhãn.
- Hoàn thiện bảng khắc phục 5 ca, mỗi loại một ca (ca 6, 20, 10, 19, 12), mỗi dòng có cách phát hiện đo được (event/đối soát, ngưỡng, tần suất) và một vai trò phụ trách.

## 4. Bằng chứng

- File: `report/team/bang_loi.md` (cột "Nhãn người 1", tỉ lệ đồng thuận, quy tắc phân biệt, bảng khắc phục).
- Commit: `a4ecb5c` (Update bang_loi.md, điền nhãn người 1) và commit cập nhật bảng khắc phục.
- Con số: đồng thuận 16/20 = 80%; 4 ca không trùng: 7, 8, 10, 13.

## 5. Công cụ AI đã dùng

- Claude Code: đọc và tóm tắt repo, đối chiếu cột "Trùng?" với hai bộ nhãn, phát hiện chỗ không nhất quán (ca 5 cùng gắn "Hệ thống" nhưng nhãn thống nhất ghi "Ngầm"; phần quy tắc và bảng khắc phục còn chép từ bài mẫu), gợi ý câu chữ cho quy tắc phân biệt và bảng khắc phục.
- Không dùng AI để gắn nhãn: cột "Nhãn người 1" do tôi tự gắn trước khi so; nhãn thống nhất do nhóm quyết định.
- Tự kiểm tra: đọc lại mô tả 20 ca trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`, đếm lại số ca không trùng, kiểm tra mỗi dòng khắc phục khớp với nhãn thống nhất và có ngưỡng đo được, người phụ trách là một vai trò.

## 6. Tự đánh giá

- Làm được: gắn nhãn độc lập, đạt đồng thuận 80%, bảng khắc phục đủ năm loại.
- Cần cải thiện: ca 8 còn tranh luận giữa "Ngầm" và "Hệ thống" (trích dẫn sai có hiện ra cho khách thấy); các ngưỡng cảnh báo trong bảng khắc phục là đề xuất, chưa kiểm chứng bằng dữ liệu đợt chạy thử.
