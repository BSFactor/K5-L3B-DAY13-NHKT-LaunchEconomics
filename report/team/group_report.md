# Báo cáo nhóm NHKT · L3B

## Mục tiêu

Đánh giá chi phí và rủi ro của trợ lý hoàn phí LogiX-VN, rồi thiết kế pilot đối chứng đủ mẫu. Nhóm dùng hai CSV giả lập gồm 1.200 yêu cầu và 1.624 lượt chạy. Vai trò và đóng góp nằm trong [TEAM.md](../../TEAM.md).

## Kết quả A–E

| Nhiệm vụ | Kết quả và ý nghĩa |
| --- | --- |
| **A · Chi phí** | Ba phép thử đạt. Chi phí **4.472 đ/việc thành công** (978 việc), cao gấp 16,3 lần hóa đơn token + tool bình quân trên yêu cầu theo cách so của đề. Quốc tế tốn 22.515 đ/việc, nên loại khỏi pilot. Nội địa và hàng nặng tốn 4.599 đ/việc ở đủ tải sau phí cố định (simulated). [Bảng A](bang_chi_phi.md#L5) |
| **B · Độ nhạy** | Làm lại gấp đôi tăng chi phí 51,8%, xem lại gấp đôi tăng 40,7%, lương tăng 25% kéo chi phí tăng 23,1%. Hai lượt chạy cho chi phí cả hệ thống thấp nhất, **6.901.220 đ** (simulated). [Bảng B](bang_chi_phi.md#L52) |
| **C · Lỗi** | Đồng thuận độc lập **16/20 (80%)**. Nhóm thống nhất bốn ca lệch và ghi cách phát hiện, cách xử lý cùng vai trò phụ trách cho năm ca đại diện. [Bảng lỗi](bang_loi.md) |
| **D · Pilot** | Chọn 20 nhân viên mỗi nhóm, phân tầng theo depot. Nhắm chênh lệch 6 điểm phần trăm, cần 299 ca đủ điều kiện/người, tương đương 859 ca hiệu dụng/nhóm. Dự kiến khoảng 10 ngày gom mẫu và thêm 7 ngày theo dõi từ ca cuối, tùy tải thực tế. [Kế hoạch pilot](pilot_plan.yaml) |
| **E · Gate 2a** | Chỉ số chính 82,83%, bỏ qua gợi ý 27,12% và mở lại 4,25% trong đợt chạy thử. Hồ sơ chốt **Go có điều kiện** cho pilot nội địa và hàng nặng. [Chỉ số và rủi ro](chi_so.md) · [Hồ sơ launch](ho_so_launch_v0.md) |

## Duyệt chéo và xử lý góp ý

Phiếu Nhóm 101 chấm NHKT ghi **20/30, Go có điều kiện** trên phiên bản họ đã xem. Bản hiện tại có đủ bảy mục và đề xuất. Với câu hỏi về phí cố định ở bước 4 người, nhóm giữ ngưỡng 6.000 đ/việc cho **chi phí biến đổi**, theo dõi 40 triệu đ/tháng riêng trong E2. Luật chênh mở lại 2 điểm áp dụng từ bước 10 người. Trần tuyệt đối 6% và dừng ngay khi hoàn trùng áp dụng ở mọi bước. Nguồn điểm là phiếu Nhóm 101 gửi NHKT. [Luật dừng cập nhật](pilot_plan.yaml)

## Hạn chế

Đợt chạy thử thiếu đối chứng nên ba chỉ số E1 chỉ mô tả dữ liệu. Cần đo phút xem lại và làm lại trong pilot. Nếu tác động thật là 5 điểm, power dự kiến chỉ khoảng 0,64. Kiểm tra cỡ mẫu thực thu ở hai nhóm trước khi đọc kết quả.
