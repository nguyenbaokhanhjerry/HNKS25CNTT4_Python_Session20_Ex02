# 1. Phân tích lỗi
# Giải thích chi tiết lỗi:
# IndexError: tuple index out of range
# ở dòng:
# mmr = record[2]
# -> Với Levi:
#    ("Levi", 120, 2500)
#    Tuple có 3 phần tử nên record[2] tồn tại.
# -> Với SofM:
#    ("SofM", 150)
#    Tuple chỉ có 2 phần tử:
#    record[0] = "SofM"
#    record[1] = 150
# -> record[2] không tồn tại nên Python phát sinh:
#    IndexError: tuple index out of range
# Giả sử sửa dữ liệu SofM thành:
# ("SofM", 150, 2800)
# Khi xử lý đến Optimus:
# ("Optimus", 100, "N/A")
# Chương trình sẽ sập ở dòng:
# int(mmr)
# Cụ thể:
# int("N/A")
# Python không thể chuyển chuỗi "N/A" thành số nguyên nên phát sinh:
# ValueError: invalid literal for int() with base 10: 'N/A'
# Kỹ năng Debug:
# Nếu thêm:
# print("Đang xử lý:", record)
# ngay dưới vòng lặp:
# for record in player_records:
# thì trước khi chương trình sập ta sẽ biết chính xác
# bản ghi nào đang được xử lý.
# Ví dụ Console:
# Đang xử lý: ('Levi', 120, 2500)
# Đang xử lý: ('SofM', 150)
#
# Sau đó chương trình báo lỗi.
# -> Nhìn vào đây có thể nhanh chóng phát hiện
#    hồ sơ của SofM bị thiếu dữ liệu.
# Đánh giá cách đặt tên biến:
# ds -> player_records
# p  -> record
# t  -> name
# m  -> matches
# r  -> mmr
# b  -> bonus
# Các tên mới giúp code dễ đọc,
# dễ bảo trì và tuân thủ chuẩn Clean Code.


# 2. Code
player_records = [
    ("Levi", 120, 2500),
    ("SofM", 150),
    ("Optimus", 100, "N/A")
]
def calculate_bonus(matches, mmr):
    return (matches * 10) + (int(mmr) * 0.5)
def process_rewards(player_records):
    print("--- BẢNG TÍNH THƯỞNG RP ---")
    for record in player_records:
        name = record[0]
        try:
            matches = record[1]
            mmr = record[2]
            bonus = calculate_bonus(matches, mmr)
            print(f"Tuyển thủ {name} nhận được {bonus} RP")
        except IndexError:
            print(f"Tuyển thủ {name}: Lỗi - Hồ sơ bị thiếu thông tin!")
            continue
        except ValueError:
            print(f"Tuyển thủ {name}: Lỗi - Dữ liệu MMR không hợp lệ!")
            continue
    print("--- HOÀN TẤT ---")
process_rewards(player_records)