# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 994/1.200 = 82,83% (phạm vi noi_dia + hang_nang: 906/982 = 92,26%) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 48/177 = 27,12% (phạm vi: 27/128 = 21,09%) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 51/1.200 = 4,25% (phạm vi: 39/982 = 3,97%) |
| Dùng | Nhóm tự đề xuất: tỉ lệ mở trợ lý của nhóm can thiệp | Số yêu cầu có `agent_suggestion_shown` mà nhân viên nhóm trợ lý mở xem, chia số yêu cầu được giao cho nhóm trợ lý | Không cần tính |
| An toàn | Nhóm tự đề xuất: tỉ lệ hoàn sai tiền qua đối soát | Số lệnh hoàn trùng mã vận đơn (ca 20) cộng số đơn lệch bảng giá trong kiểm tra mẫu (ca 5, 12, 17), chia số lệnh hoàn được đối soát trong tuần | Không cần tính |

Chỉ số chính trong đợt chạy thử là 82,83%. Không viết "trợ lý đã nâng chỉ số từ 0,70": đợt chạy thử không có nhóm đối chứng. Ba chỉ số trên dùng các cột kết quả của bộ dữ liệu giả lập, không dùng cột phút `_simulated`.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | Ứng dụng khách | request_id, created_at, loai, so_tien_vnd, depot, staff_id, arm (tro_ly / doi_chung), trace_id | Khi khách gửi yêu cầu |
| `agent_run_completed` | Agent | attempt, tokens_in, tokens_out, tool_calls, status, trace_id | Sau mỗi lần chạy, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | staff_id, so_tien_de_xuat, opened (có/không), trace_id | Khi gợi ý hiện ra và khi nhân viên mở, đếm theo yêu cầu duy nhất |
| `staff_review_decision` | Nhân viên | quyet_dinh (giu / sua / bo), phut_xem_lai đo thật, trace_id | Khi nhân viên bấm gửi, sửa hoặc bỏ |
| `staff_rework_completed` | Nhân viên | phut_lam_lai đo thật, ly_do, trace_id | Khi làm lại xong |
| `handoff_to_staff` | Agent | reason (thieu_du_lieu, ngoai_12_thang, ngoai_pham_vi…), tom_tat, trace_id | Khi agent chuyển ca cho nhân viên |
| `refund_ledger_write` | Dịch vụ sổ cái | idempotency_key, ma_van_don, so_tien, ket_qua (ok / loi), trace_id | Khi ghi lệnh hoàn vào sổ cái |
| `ticket_closed` | Hệ thống ticket | closed_at, trace_id | Khi yêu cầu đóng |
| `ticket_reopened` | Khách | reopened_at, ly_do, trace_id | Khi khách mở lại yêu cầu |
| `audit_sample_checked` | Kế toán | so_tien_da_hoan, so_tien_dung, phien_ban_bang_gia, trace_id | Hằng tuần, mẫu 100 đơn |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- Chính: `refund_request_created` (mẫu số, thời điểm gửi) + `ticket_closed` (đóng trong 24 giờ) + `ticket_reopened` (mở lại trong 7 ngày).
- Dùng · bỏ qua gợi ý: `staff_review_decision` (sua hoặc bo, chia tổng số decision).
- An toàn · lỗi lọt đến khách: `ticket_reopened` chia `refund_request_created`.
- Dùng · tỉ lệ mở trợ lý: `agent_suggestion_shown.opened` chia `refund_request_created` có arm = tro_ly.
- An toàn · hoàn sai tiền: `refund_ledger_write` (chỉ lệnh thành công, đếm hoàn trùng) + `audit_sample_checked` (lệch bảng giá). Đếm lệnh lỗi duy nhất trong tập lệnh đã đối soát, gộp hai nhóm và loại trùng.
- Chi phí mỗi việc thành công: `agent_run_completed` (token, tool) + `staff_review_decision` và `staff_rework_completed` (phút đo thật thay cho hai cột `_simulated`).
- Cả năm chỉ số đều tính được từ danh sách event.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | B1: chi phí mỗi việc thành công +51,8%, từ 4.472 đ lên 6.787 đ (simulated) | Tỉ lệ `ket_qua = lam_lai` theo tuần vượt 8% (đợt chạy thử: 48/982 = 4,89% trong phạm vi) | Rà 20 trace làm lại gần nhất theo `trace_id`; nếu vẫn vượt 2 tuần thì thu hẹp về noi_dia | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | B4: 11.743 đ/việc = 0,98× mức 12.000 đ tự làm; 12.414 đ = 1,03× nếu làm lại 15,3 phút như dữ liệu (simulated) | Tỉ lệ yêu cầu được xem lại vẫn trên 50% ở cuối bước rollout 0.25 (đợt chạy thử: 128/982 = 13,03%) | Giảm xem lại theo bậc khi tỉ lệ bỏ qua gợi ý dưới 15% trong 2 tuần | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | A4: chi phí cố định 40 triệu đ/tháng là 1.185 đ/việc ở 45.000 yêu cầu/tháng, 2.370 đ/việc nếu còn một nửa; tổng 5.784 đ/việc (simulated) | Số việc thành công theo tuần dưới 50% kế hoạch (33.750 việc/tháng ≈ 7.800 việc/tuần, tức dưới khoảng 3.900 việc/tuần) | Không mở rộng pilot; xem lại hợp đồng chi phí cố định trước ngày quyết định | Giám đốc vận hành LogiX-VN |
