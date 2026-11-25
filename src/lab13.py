"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
from statistics import NormalDist

import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if not 0 < p <= 1:
        raise ValueError('p phải nằm trong khoảng (0, 1]')
    if k is not None:
        if k < 1:
            raise ValueError('k phải ít nhất bằng 1')
        return (1 - (1 - p) ** k) / p
    return 1 / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if not 0 < p <= 1:
        raise ValueError('p phải nằm trong khoảng (0, 1]')
    if k is None:
        return 1.0
    if k < 1:
        raise ValueError('k phải ít nhất bằng 1')
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])].copy()

    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay].copy()
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = (runs['tokens_in'] / 1000 * gia_vao
                  + runs['tokens_out'] / 1000 * gia_ra)
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = (reqs['ket_qua'] == 'thanh_cong').sum()

    if thanh_cong == 0:
        cps = math.inf
    else:
        cps = tong / thanh_cong

    return dict(
        token=tien_token.sum(),
        tool=tien_tool.sum(),
        chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        cps=cps,
        hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs),
    )


def co_mau_hai_ty_le(p1, p2, alpha=0.05, power=0.8):
    """Cỡ mẫu mỗi nhóm khi so sánh hai tỷ lệ với phân bổ 1:1."""
    normal = NormalDist()
    p_trung_binh = (p1 + p2) / 2
    thanh_phan_alpha = normal.inv_cdf(1 - alpha / 2) * math.sqrt(
        2 * p_trung_binh * (1 - p_trung_binh)
    )
    thanh_phan_power = normal.inv_cdf(power) * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))
    return math.ceil(((thanh_phan_alpha + thanh_phan_power) / (p2 - p1)) ** 2)


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:12s} {gia_tri:>14,.0f}')
    # TODO CP1 · Nhiệm vụ A3: tính lại theo từng giá trị của cột loai.
    print('\nA3 · Theo loại yêu cầu')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        req_loai = reqs[reqs['loai'] == loai]
        kq = mo_hinh(runs, req_loai)
        tong_lan_chay = req_loai['so_lan_chay'].sum()
        print(f"{loai:10s} {len(req_loai):4d} yêu cầu | "
              f"thành công {kq['thanh_cong'] / len(req_loai):.1%} | "
              f"chạy/yêu cầu {tong_lan_chay / len(req_loai):.2f} | "
              f"cps {kq['cps']:,.0f} đ | "
              f"so với 12.000 đ {kq['cps'] / BASELINE:.2f}x")

    # TODO CP2 · Nhiệm vụ B: đổi từng yếu tố, ghi vào bảng độ nhạy.
    print('\nB1 · Độ nhạy')
    kich_ban = {
        'Giá token gấp đôi': dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
        'Xem lại gấp đôi': dict(he_so_xem_lai=2),
        'Xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Làm lại gấp đôi': dict(he_so_lam_lai=2),
        'Làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương nhân viên tăng 25%': dict(luong_phut=2500),
        'Chỉ cho chạy tối đa 2 lần': dict(max_lan_chay=2),
        'Chỉ cho chạy 1 lần': dict(max_lan_chay=1),
    }
    goc_cps = ket_qua['cps']
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        print(f"{ten:29s} {cps:10,.0f} đ | {(cps / goc_cps - 1) * 100:+6.1f}%")

    print('\nB2 · Tác động cặp')
    cps_cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260,
                      he_so_xem_lai=2)['cps']
    print(f"Token gấp đôi + xem lại gấp đôi: {cps_cap:,.0f} đ | "
          f"{(cps_cap / goc_cps - 1) * 100:+.1f}%")

    print('\nB3 · Giới hạn chạy lại')
    for gioi_han in [1, 2, 3]:
        kq = mo_hinh(runs, reqs, max_lan_chay=gioi_han)
        khong_thanh_cong = len(reqs) - kq['thanh_cong']
        he_thong = kq['tong'] + BASELINE * khong_thanh_cong
        print(f"{gioi_han} lần | trợ lý {kq['tong']:,.0f} đ | "
              f"không thành công {khong_thanh_cong} | "
              f"cả hệ thống {he_thong:,.0f} đ | cps {kq['cps']:,.0f} đ")

    print('\nB4 · Xem lại 100% trong noi_dia + hang_nang')
    pilot_req = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])].copy()
    pilot_runs = runs[runs['request_id'].isin(pilot_req['request_id'])].copy()
    da_ok = pilot_runs[pilot_runs['status'] == 'ok']['request_id'].nunique()
    xem_phut = da_ok * 5
    lam_phut = (pilot_req[pilot_req['ket_qua'] == 'lam_lai'].shape[0] * 9)
    token_tool = ((pilot_runs['tokens_in'] / 1000 * GIA_VAO
                   + pilot_runs['tokens_out'] / 1000 * GIA_RA
                   + pilot_runs['tool_calls'] * GIA_TOOL).sum())
    thanh_cong = (pilot_req['ket_qua'] == 'thanh_cong').sum()
    tong_b4 = token_tool + xem_phut * LUONG_PHUT + lam_phut * LUONG_PHUT
    cps_b4 = tong_b4 / thanh_cong
    print(f"{cps_b4:,.0f} đ/việc thành công | {cps_b4 / BASELINE:.2f}x")

    print('\nA4 · Chi phí cố định trong phạm vi noi_dia + hang_nang')
    noi_dia_hang_nang = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])].copy()
    kq_scope = mo_hinh(runs, noi_dia_hang_nang)
    for mo_ta, yeu_cau_thang, viec_thanh_cong in [
        ('45.000 yêu cầu/tháng', 45000, 33750),
        ('Một nửa khối lượng', 22500, 16875),
    ]:
        cps_scope = kq_scope['tong'] / kq_scope['thanh_cong']
        fixed_per_success = 40_000_000 / viec_thanh_cong
        cps_fixed = cps_scope + fixed_per_success
        print(f"{mo_ta}: {viec_thanh_cong:,} việc thành công | "
              f"cố định {fixed_per_success:,.0f} đ/việc | "
              f"cps + cố định {cps_fixed:,.0f} đ | "
              f"{cps_fixed / BASELINE:.2f}x")
    print('\nD1 · Cỡ mẫu pilot')
    baseline = 0.70
    icc = 0.02
    ca_moi_nhan_vien = 75
    nhan_vien_moi_nhom = 20
    depot_moi_nhom = 6

    n_5_diem = co_mau_hai_ty_le(baseline, 0.75)
    he_so_thiet_ke = 1 + (ca_moi_nhan_vien - 1) * icc
    n_theo_nhan_vien = math.ceil(n_5_diem * he_so_thiet_ke)
    so_nhan_vien = math.ceil(n_theo_nhan_vien / ca_moi_nhan_vien)
    n_6_diem = co_mau_hai_ty_le(baseline, 0.76)
    # Giải c*m / (1 + (m - 1)*ICC) >= n cho m.
    ca_can_moi_nhan_vien = math.ceil(
        n_6_diem * (1 - icc) / (nhan_vien_moi_nhom - n_6_diem * icc)
    )
    de_6_diem = 1 + (ca_can_moi_nhan_vien - 1) * icc

    print(f'a) Chia theo yêu cầu: {n_5_diem:,} yêu cầu/nhóm')
    print(f'b) Chia theo nhân viên, m = {ca_moi_nhan_vien}: DE = {he_so_thiet_ke:.2f}, '
          f'{n_theo_nhan_vien:,} yêu cầu/nhóm, {so_nhan_vien} nhân viên/nhóm')
    print(f'c) {nhan_vien_moi_nhom} nhân viên/nhóm: '
          f'cỡ mẫu hiệu dụng < {nhan_vien_moi_nhom / icc:,.0f}/nhóm')
    print(f'd) {depot_moi_nhom} depot/nhóm: '
          f'cỡ mẫu hiệu dụng < {depot_moi_nhom / icc:,.0f}/nhóm')
    print(f'e) +6 điểm: {n_6_diem} yêu cầu hiệu dụng/nhóm, '
          f'ít nhất {ca_can_moi_nhan_vien} yêu cầu/nhân viên, DE = {de_6_diem:.2f}')

    print('\nCP4 · Tỷ lệ mở lại trong 7 ngày')
    for pham_vi, yeu_cau in [('Toàn mẫu', reqs), ('noi_dia + hang_nang', pilot_req)]:
        mo_lai = yeu_cau['mo_lai_trong_7_ngay']
        print(f'{pham_vi}: {mo_lai.sum():.0f}/{len(mo_lai):,} = {mo_lai.mean():.2%}')

    yeu_cau_moi_ngay = 1500
    tong_nhan_vien = 2 * nhan_vien_moi_nhom
    ty_le_trong_pham_vi = len(pilot_req) / len(reqs)
    ca_pilot_moi_nguoi_ngay = yeu_cau_moi_ngay * ty_le_trong_pham_vi / tong_nhan_vien
    ngay_gom_mau = math.ceil(ca_can_moi_nhan_vien / ca_pilot_moi_nguoi_ngay)
    theo_doi_mo_lai = 7
    print('\nCP4 · Ước tính thời gian gom mẫu ở bước 20 nhân viên mỗi nhóm')
    print(f'{nhan_vien_moi_nhom * ca_can_moi_nhan_vien:,} yêu cầu thực tế mỗi nhóm')
    print(f'{ca_pilot_moi_nguoi_ngay:.2f} yêu cầu trong phạm vi/người/ngày '
          f'với giả định tải chia đều')
    print(f'Khoảng {ngay_gom_mau} ngày gom mẫu + {theo_doi_mo_lai} ngày theo dõi '
          f'từ ca cuối = {ngay_gom_mau + theo_doi_mo_lai} ngày kể từ bước đủ hai nhóm')
