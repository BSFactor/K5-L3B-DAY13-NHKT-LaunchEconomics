# Báo cáo cá nhân — Nguyễn Minh Thành

## 1. Thông tin thành viên

- Họ tên: Nguyễn Minh Thành
- MSSV: 2A202603884
- Vai trong nhóm: Người viết code (`src/lab13.py`).

## 2. Phần việc phụ trách

Phụ trách phần code của nhóm trong `src/lab13.py`, chạy chương trình và chuẩn bị giải thích các phép tính, kết quả do code tạo ra. Không phụ trách các hồ sơ và báo cáo nhóm khác.

## 3. Đóng góp cụ thể

- Viết và chạy `src/lab13.py`: kiểm tra công thức số lần chạy kỳ vọng và xác suất thành công; xây dựng mô hình chi phí token, tool, xem lại và làm lại.
- Dùng chương trình để phân tích chi phí theo loại yêu cầu, các kịch bản độ nhạy, giới hạn số lần chạy lại, chi phí cố định và cỡ mẫu/thời gian pilot.
- Đối chiếu kết quả chạy của code với các con số trong báo cáo nhóm; chuẩn bị giải thích giả định và giới hạn của các phép tính.

## 4. Bằng chứng

- Chương trình `src/lab13.py` chạy thành công; ba phép thử đáp án biết trước đều đạt.
- Kết quả kiểm tra: 1.200 yêu cầu, 1.624 lần chạy; 978 yêu cầu thành công; tổng chi phí 4.373.585 đ và CPS khoảng 4.472 đ/việc thành công. Các khoản phút xem lại/làm lại là dữ liệu `simulated`.
- Báo cáo chi tiết: `report/team/bang_chi_phi.md`; các kết quả trên cũng được in khi chạy `python3 lab13.py` trong `src/`.

## 5. Công cụ AI đã dùng

Copilot được dùng để hỗ trợ rà soát mã, giải thích kết quả và soạn bản nháp này. Kết quả số được đối chiếu bằng cách chạy trực tiếp `python3 lab13.py` trong thư mục `src/`; tôi chịu trách nhiệm kiểm tra lại code và kết quả trước khi nộp.

## 6. Ghi chú chuẩn bị hỏi đáp

### Nhóm đã triển khai gì?

Đây là bài phân tích kinh tế và lập kế hoạch pilot cho trợ lý hoàn phí LogiX-VN, không phải một dịch vụ production. Mã đọc hai CSV giả lập, tính chi phí mỗi yêu cầu thành công, tách kết quả theo bốn loại yêu cầu, thử độ nhạy với giá/nhân công/số lần chạy lại, và ước tính cỡ mẫu cùng thời gian thu thập cho pilot. Không cần API key.

### Các con số chính là gì?

- CPS chung khoảng **4.472 đ/việc thành công**, so với **12.000 đ** nếu nhân viên tự xử lý; con số này chưa gồm chi phí cố định.
- Theo loại: `noi_dia` **2.696 đ**, `hang_nang` **8.221 đ**, `quoc_te` **22.515 đ**, `doi_tac` **10.215 đ** mỗi việc thành công. Vì vậy quốc tế là nhóm kém hiệu quả nhất trong dữ liệu; không nên suy rộng kết quả trung bình cho mọi loại.
- Làm lại và xem lại là các yếu tố độ nhạy lớn nhất: làm lại gấp đôi làm CPS tăng **51,8%**; xem lại gấp đôi tăng **40,7%**. Các phút xem lại/làm lại là `simulated`.
- Khi tính cả chi phí xử lý yêu cầu không thành công theo baseline, giới hạn **2 lần chạy** có tổng chi phí hệ thống thấp nhất trong ba kịch bản đã thử: **6.901.220 đ**. Giới hạn 1 lần có CPS của các ca thành công thấp nhất, nhưng để lại nhiều ca thất bại hơn.
- Cỡ mẫu để phát hiện mức tăng 5 điểm phần trăm là khoảng **1.251 yêu cầu/nhóm** nếu chia ngẫu nhiên theo yêu cầu. Chia theo cụm nhân viên làm tăng nhu cầu mẫu; ước tính hiện tại với 20 nhân viên/nhóm cần khoảng **299 yêu cầu/nhân viên** và khoảng **17 ngày** gồm thu thập cùng theo dõi mở lại.

### Những giới hạn cần nói rõ?

- Tất cả dữ liệu mẫu và giá trong lab là giả định/giả lập; đặc biệt thời gian xem lại và làm lại không phải phép đo vận hành thực tế.
- CPS không đồng nghĩa với tổng chi phí dài hạn: báo cáo A4 mới cộng riêng khoản cố định theo giả định về lưu lượng và tỉ lệ thành công.
- Chạy thử không có nhóm đối chứng nên chưa chứng minh agent làm tăng hiệu quả so với hiện trạng.
- Hồ sơ hiện còn chưa hoàn chỉnh: `pilot_plan.yaml` vẫn còn dấu `?`; `chi_so.md` và `ho_so_launch_v0.md` còn các mục `...`/chưa chốt, gồm ngưỡng an toàn và đề xuất cuối. Không nên trình bày kế hoạch hay quyết định Gate 2a như đã được chốt.

## 7. Tự đánh giá

Tôi có thể giải thích luồng code, cách tính CPS, sự khác nhau giữa CPS và tổng chi phí hệ thống, cùng các giả định của phép tính. Tôi chỉ nhận trách nhiệm phần code; các hồ sơ khác do thành viên được phân công phụ trách.
