# Phiếu chấm hội đồng Gate 2a

- **Nhóm chấm:** NHKT · L3B
- **Nhóm được chấm:** TLiet · L3B
- **Hồ sơ đối chiếu:** [Hồ sơ launch v0](https://github.com/ArthurTheMana/K5-L3B-DAY13-TLiet-LaunchEconomics/blob/34c17ed282373a3a47c452c55e942eb3889e5d96/report/team/ho_so_launch_v0.md) · [Kế hoạch pilot](https://github.com/ArthurTheMana/K5-L3B-DAY13-TLiet-LaunchEconomics/blob/34c17ed282373a3a47c452c55e942eb3889e5d96/report/team/pilot_plan.yaml)

| Tiêu chí | Điểm | Lý do |
| --- | ---: | --- |
| Đề xuất khớp bằng chứng | 10/10 | Go có điều kiện phù hợp với CPS **4.599 đ/việc** ở đủ tải (simulated). Hồ sơ nêu cả số bất lợi: xem lại 100% có thể đẩy CPS lên **12.415 đ**, vượt mốc 12.000 đ nhân viên tự xử lý. |
| Số giả lập và phạm vi | 10/10 | Hồ sơ ghi nhãn simulated và giới hạn pilot ở `noi_dia` (**2.696 đ/việc**) và `hang_nang` (**8.221 đ/việc**). `quoc_te` tốn **22.515 đ/việc**, còn `doi_tac` có điều khoản riêng. |
| Pilot ra được quyết định | 10/10 | Chia ngẫu nhiên theo nhân viên, phân tầng theo depot, đối chứng đồng thời, **20 cụm mỗi nhóm**, **299 yêu cầu/người**, tương đương khoảng **859 mẫu hiệu dụng/nhóm** để phát hiện chênh 6 điểm. Có ba luật dừng với ngưỡng, thời hạn và người xử lý. |
| **Tổng** | **30/30** | |

**Quyết định của hội đồng: Go có điều kiện** cho pilot trong phạm vi đã nêu. Chốt cách tính và theo dõi CPS theo từng loại yêu cầu trước khi bắt đầu.

## Câu hỏi dành cho đội trình bày

Trong báo cáo, nhóm đưa cả `noi_dia` và `hang_nang` vào pilot. Chi phí mỗi yêu cầu thành công của `hang_nang` là **8.221 đ**, vượt ngưỡng **8.000 đ** trong luật dừng pilot.

Vì sao nhóm vẫn đưa `hang_nang` vào pilot ngay từ đầu? Khi quyết định có tiếp tục, nhóm sẽ dùng CPS theo từng loại yêu cầu hay CPS bình quân của toàn pilot?

## Câu trả lời dự kiến của đội trình bày

Nhóm đưa `hang_nang` vào pilot để kiểm chứng khả năng của trợ lý trên nhiều loại yêu cầu. `noi_dia` có hiệu quả kinh tế tốt hơn trong dữ liệu hiện có.

Mức **8.221 đ** là kết quả mô phỏng ban đầu. Pilot sẽ dùng số phút xem lại và làm lại đo được để đánh giá CPS trong điều kiện vận hành thực tế.

Nhóm dự kiến theo dõi CPS riêng cho từng loại bên cạnh CPS bình quân. Nếu CPS đo được của `hang_nang` vượt **8.000 đ trong hai tuần liên tiếp**, nhóm sẽ thu hẹp pilot về `noi_dia`, theo hành động thu hẹp phạm vi trong luật dừng.

**Đánh giá của hội đồng:** Câu trả lời hợp lý nếu TLiet ghi rõ trong kế hoạch rằng ngưỡng được kiểm riêng cho `hang_nang`. YAML hiện ghi ngưỡng 8.000 đ nhưng chưa chỉ rõ áp dụng theo loại hay toàn pilot. Theo dõi riêng giúp tránh việc chi phí thấp của `noi_dia` che lấp mức vượt ngưỡng ở `hang_nang`.

_Câu trả lời trên là dự kiến. Phản hồi thực tế của TLiet chờ xác nhận._
