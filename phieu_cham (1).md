# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): Nhóm 101 — Đào Vũ Minh Khánh (TV3), Nguyễn Văn Quốc (TV4)
- Nhóm được chấm: NHKT (repo `BSFactor/K5-L3B-DAY13-NHKT-LaunchEconomics`). Điểm dưới đây chấm trên commit `6f357f6`.

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Đề xuất Go có điều kiện khớp số A4 (4.599 đ/việc kể cả cố định, simulated). Nêu hai con số bất lợi kèm cách xử lý: power chỉ 0,64 nếu tác động thật là 5 điểm → Giám đốc vận hành ký chấp nhận trước 2026-12-04; xem lại 100% tốn 11.743 đ và vượt 12.000 đ nếu làm lại 15,3 phút [simulated] → kế hoạch giảm xem lại theo bậc, kiểm tra 2026-12-21. 4 điều kiện đều có một vai trò và ngày kiểm tra |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Nhãn `simulated` ở mọi số từ cột giả lập; `simulated_inputs` liệt kê 10 đầu vào. Phạm vi noi_dia (2.696 đ = 0,22×) + hang_nang (8.221 đ = 0,69×), loại quoc_te (22.515 đ = 1,88×, thành công 27,3%) và doi_tac (thành công 54,4%) [simulated]; chỉ số dùng tách toàn mẫu 27,12% và trong phạm vi 21,1% |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Chia theo nhân viên 20 + 20, bốc thăm có seed, phân tầng theo depot; 859 hiệu dụng/nhóm (DE 6,96; 299 yêu cầu/người), MDE 6 điểm có ghi đánh đổi. 3 luật dừng có ngưỡng, thời hạn và người dừng; luật an toàn chỉ so chênh 2 điểm từ bước 10 người (trần 6% và hoàn trùng áp ở mọi bước), luật chi phí 6.000 đ chỉ tính chi phí biến đổi, 40 triệu cố định theo dõi riêng trong E2. Rollback 30 phút; quyết định 2027-01-08 |
| **Tổng** | | | | **30 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Hồ sơ đủ 7 mục, đề xuất khớp số và nêu thẳng con số bất lợi (power 0,64 ở mức 5 điểm; xem lại 100% tốn 11.743–12.414 đ [simulated]); pilot tách được tác động với 20 cụm/nhóm và 3 luật dừng cụ thể. Điều kiện theo hồ sơ của nhóm, thêm một điều: bỏ từ "production" ở dòng 33 của `report/team/2A202603884_NguyenMinhThanh.md` (quy tắc cấm dùng từ này trong `report/team/`).

**Một câu hỏi cho đội trình:** Ở bước 4 người, 40 triệu đ/tháng cố định chia cho số việc thành công đã khoảng 11.900 đ/việc, vượt ngưỡng 6.000 đ của luật chi phí ngay tuần đầu. Nhóm xử lý thế nào để luật không dừng pilot chỉ vì khối lượng còn ít?

**Câu trả lời của đội trình (ghi lại tại buổi):** Chưa có bản ghi tại buổi.

**Trả lời theo kế hoạch pilot đã cập nhật:** NHKT áp dụng ngưỡng 6.000 đ/việc cho chi phí biến đổi gồm token, tool, giờ xem lại và giờ làm lại. Theo dõi riêng 40 triệu đ/tháng trong E2 để đánh giá ảnh hưởng của khối lượng. Như vậy, việc phân bổ phí cố định lên số đơn ít ở bước 4 người không tự kích hoạt luật dừng. Nếu chi phí biến đổi vượt 6.000 đ/việc trong hai tuần liên tiếp, PM thu hẹp về `noi_dia` và giới hạn tối đa hai lần chạy.
