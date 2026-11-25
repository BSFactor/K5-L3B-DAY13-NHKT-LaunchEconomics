# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Nguyễn Trọng Nghĩa · Người gắn nhãn 2: Nguyễn Văn Hùng (gắn trong 8 phút, không trao đổi)

|  Ca | Nhãn người 1      | Nhãn người 2      | Trùng? | Nhãn thống nhất   |
| --: | ----------------- | ----------------- | ------ | ----------------- |
|   1 | Do người dùng     | Do người dùng     | Có     | Do người dùng     |
|   2 | Hệ thống          | Hệ thống          | Có     | Hệ thống          |
|   3 | Ngữ cảnh          | Ngữ cảnh          | Có     | Ngữ cảnh          |
|   4 | Giới hạn hệ thống | Giới hạn hệ thống | Có     | Giới hạn hệ thống |
|   5 | Hệ thống          | Hệ thống          | Có     | Hệ thống          |
|   6 | Do người dùng     | Do người dùng     | Có     | Do người dùng     |
|   7 | Giới hạn hệ thống | Hệ thống          | Không  | Hệ thống          |
|   8 | Ngầm              | Hệ thống          | Không  | Ngầm              |
|   9 | Do người dùng     | Do người dùng     | Có     | Do người dùng     |
|  10 | Ngữ cảnh          | Giới hạn hệ thống | Không  | Ngữ cảnh          |
|  11 | Giới hạn hệ thống | Giới hạn hệ thống | Có     | Giới hạn hệ thống |
|  12 | Ngầm              | Ngầm              | Có     | Ngầm              |
|  13 | Giới hạn hệ thống | Ngữ cảnh          | Không  | Giới hạn hệ thống |
|  14 | Do người dùng     | Do người dùng     | Có     | Do người dùng     |
|  15 | Hệ thống          | Hệ thống          | Có     | Hệ thống          |
|  16 | Ngữ cảnh          | Ngữ cảnh          | Có     | Ngữ cảnh          |
|  17 | Ngầm              | Ngầm              | Có     | Ngầm              |
|  18 | Ngữ cảnh          | Ngữ cảnh          | Có     | Ngữ cảnh          |
|  19 | Giới hạn hệ thống | Giới hạn hệ thống | Có     | Giới hạn hệ thống |
|  20 | Hệ thống          | Hệ thống          | Có     | Hệ thống          |

**Tỉ lệ đồng thuận:** 16 / 20 = 80%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

Ca không trùng: 7, 8, 10, 13 (4 ca), đồng thuận 16/20 = 80%, đạt ngưỡng nên không phải viết lại định nghĩa.

- Ca 7 (Giới hạn hệ thống / Hệ thống → Hệ thống): lỗi 503 là giới hạn hạ tầng, nhưng gốc lỗi là trợ lý báo "đã hoàn tiền thành công" trái thiết kế; còn báo đúng "chưa xử lý được" thì mới là giới hạn.
- Ca 8 (Ngầm / Hệ thống → Ngầm): số tiền hoàn vẫn đúng nên khách và nhân viên không có lý do phản ánh; trích dẫn sai chỉ lộ ra khi đối chiếu với bản chính sách hiện hành.
- Ca 10 (Ngữ cảnh / Giới hạn hệ thống → Ngữ cảnh): trợ lý làm được và làm đúng chính sách bất khả kháng; sai ở chỗ khách dựa vào cam kết "giao 24 giờ", tức giả định không khớp hoàn cảnh.
- Ca 13 (Giới hạn hệ thống / Ngữ cảnh → Giới hạn hệ thống): bảo hiểm hàng hoá nằm ngoài phạm vi trợ lý, nên là giới hạn, kể cả khi trợ lý xử lý giới hạn đó kém (trả lời chung chung).

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 6 | Do người dùng | Event `category_mismatch` (mục khách chọn khác nhãn trợ lý phân loại từ mô tả) kèm `trace_id`; báo cáo hằng ngày, cảnh báo khi >3% yêu cầu/ngày | Trợ lý đối chiếu mục đã chọn với nội dung mô tả; lệch thì hỏi lại khách "Bạn muốn báo giao trễ hay hàng bị vỡ?" trước khi từ chối | PM trợ lý hoàn phí |
| 20 | Hệ thống | Đối soát sổ cái mỗi giờ: hai lệnh hoàn trở lên cho cùng mã vận đơn, khác `trace_id`; ngưỡng 0 ca, có ca là chặn ngay | Bắt buộc khoá chống trùng (idempotency key = mã vận đơn + loại hoàn) ở bước ghi sổ cái; yêu cầu gửi lại trong lúc đang xử lý thì trả trạng thái "đang xử lý" | Kỹ sư trưởng agent |
| 10 | Ngữ cảnh | Tỉ lệ `mo_lai_trong_7_ngay` của các ca từ chối vì bất khả kháng, tính theo tuần; cảnh báo khi >10% | Tin nhắn từ chối trích điều khoản bất khả kháng và nói rõ cam kết 24 giờ không áp dụng khi có thiên tai; đề xuất đội sản phẩm ẩn cam kết 24 giờ trên ứng dụng khi có cảnh báo bão | Trưởng nhóm CSKH |
| 19 | Giới hạn hệ thống | Event `handoff_to_staff` với `reason=ngoai_12_thang` kèm `trace_id`; theo dõi số ca/tuần và thời gian nhân viên đóng ca sau khi nhận, cảnh báo khi >24 giờ | Giữ cách nói rõ giới hạn và chuyển kèm tóm tắt; kiểm tra ngày đơn ngay ở bước đầu để chuyển luôn, không gọi tool tra đơn | PM trợ lý hoàn phí |
| 12 | Ngầm | So token/yêu cầu và `tool_calls`/lần chạy theo depot từ `logix_runs.csv`, chạy hằng ngày; cảnh báo khi một depot vượt 1,5 lần trung vị các depot 2 ngày liên tiếp | Tool tra đơn kiểm tra đủ trường và trả lỗi rõ khi thiếu, thay vì để trợ lý gọi lại nhiều lần; đặt trần số lần gọi tool cho mỗi yêu cầu | Kỹ sư trưởng agent |
