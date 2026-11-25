# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: NHKT · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | CPS 4.472 đ/việc thành công (978 việc; tổng chi phí 4.373.585 đ; simulated; chưa gồm chi phí cố định) | Giả lập | Người viết code |
| 2 · Ba yếu tố nhạy nhất | Làm lại gấp đôi: +51,8%; xem lại gấp đôi: +40,7%; lương tăng 25%: +23,1% (simulated) | Giả lập | Người kiểm số |
| 3 · So với nhân viên tự làm | A4 (noi_dia + hang_nang): 4.599 đ/việc ở 45.000 YC/tháng; 5.784 đ/việc ở 22.500 YC/tháng (simulated), dưới 12.000 đ/YC tự làm; chưa cộng chi phí xử lý ca không thành công | Giả lập | Người gắn nhãn 2, kiêm giữ hồ sơ |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Trong đợt chạy thử (không có đối chứng): chính 82,83% (994/1.200); bỏ qua gợi ý 27,12% (48/177); mở lại 7 ngày 4,25% (51/1.200). Thêm 2 chỉ số tự đề xuất và 10 event có trace_id, kiểm tra chéo đủ (`chi_so.md`) | Xong, có bằng chứng | Người kiểm số |
| 5 · Bảng lỗi và cách khắc phục | Người gắn nhãn 1 và 2 đồng thuận 16/20 ca (80%); 4 ca bất đồng (7, 8, 10, 13) đã thống nhất; 5 ca khắc phục đủ 5 loại, có cách phát hiện đo được và một vai trò phụ trách | Xong, có bằng chứng | Người gắn nhãn 1 |
| 6 · Pilot plan | Chia theo nhân viên 20 + 20, ngẫu nhiên phân tầng theo depot; phạm vi noi_dia + hang_nang; mức chênh 6 điểm (859 ca hiệu dụng/nhóm, DE 6,96, ≥ 299 yêu cầu/người); power chỉ còn 0,64 nếu tác động thật là 5 điểm; 4 luật dừng (an toàn tách sự cố hoàn trùng dừng ngay và tỉ lệ mở lại đánh giá theo tuần; chi phí; sử dụng); baseline 0,70 theo đề, đo lại cho phạm vi pilot trước ngày bắt đầu; quyết định 2027-01-08 (`pilot_plan.yaml`) | Xong, có bằng chứng | Người gắn nhãn 1 |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi: CPS 6.787 đ (+51,8%); xem lại 100%: CPS 11.743 đ (0,98× mức 12.000 đ/YC tự làm), tăng lên 12.414 đ nếu làm lại 15,3 phút (1,03×; simulated). 3 dòng rủi ro có ngưỡng theo dõi và người phụ trách trong E2 (`chi_so.md`). | Giả lập | Người kiểm số |

Điều kiện duyệt pilot cho noi_dia + hang_nang (4.599 đ/việc thành công kể cả cố định ở đủ tải, simulated). Loại quoc_te và doi_tac khỏi phạm vi.

- Có khoá chống trùng và đối soát sổ cái mỗi giờ (ca 7, 20), chạy thử đạt 0 ca hoàn trùng · Kỹ sư trưởng agent · kiểm tra 2026-12-04.
- Giám đốc vận hành ký chấp nhận mức chênh 6 điểm (859 ca hiệu dụng/nhóm; power chỉ 0,64 nếu tác động thật là 5 điểm) · Giám đốc vận hành LogiX-VN · kiểm tra 2026-12-04.
- Kiểm tra 10 event trước khi mở pilot ngày 2026-12-07. Sau tuần 1, dùng phút đo từ `staff_review_decision` và `staff_rework_completed` để tính lại chi phí biến đổi · PM trợ lý hoàn phí · kiểm tra 2026-12-04 và 2026-12-14.
- Có kế hoạch giảm xem lại theo bậc. B4 đạt 11.743 đ/việc ở giả định 9 phút làm lại và vượt 12.000 đ nếu làm lại mất 15,3 phút · Trưởng nhóm CSKH · kiểm tra 2026-12-21 trước bước 20 người.

**Đề xuất: Go có điều kiện** cho pilot. Giữ ngưỡng mở lại tuyệt đối 6% ở mọi bước, so chênh 2 điểm từ bước 10 người, và dùng ngưỡng 6.000 đ cho chi phí biến đổi.
