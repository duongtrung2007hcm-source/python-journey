"""
Bài tập 02: Chuyển đổi kiểu dữ liệu 🔄
=========================================
Mục tiêu: Thành thạo int(), float(), str(), bool()
"""

# 1. Cho so_text = "42"
# Chuyển sang int, cộng thêm 8, in kết quả
so_text = "42"
so = int(so_text)
ket_qua = so + 8
print("42 + 8 =", ket_qua)


# 2. Cho pi = 3.14159
# Chuyển sang int (sẽ được bao nhiêu?), in kết quả
pi = 3.14159
pi_nguyen = int(pi)
print("int(pi) =", pi_nguyen)


# 3. Kiểm tra bool() của các giá trị sau và in kết quả
# bool(0), bool(1), bool(""), bool("hello"), bool([]), bool([1,2])
print("bool(0):", bool(0))
print("bool(1):", bool(1))
print('bool(""):', bool(""))
print('bool("hello"):', bool("hello"))
print("bool([]):", bool([]))
print("bool([1, 2]):", bool([1, 2]))


# 4. Nhập chiều cao (m) và cân nặng (kg) từ người dùng
# Tính BMI = cân_nặng / (chiều_cao ** 2)
# In ra BMI với 1 chữ số thập phân
chieu_cao = float(input("Nhập chiều cao (m): "))
can_nang = float(input("Nhập cân nặng (kg): "))
if chieu_cao != 0:
    bmi = can_nang / (chieu_cao**2)
    print(f"BMI của bạn: {bmi:.1f}")
else:
    print("Chiều cao phải khác 0 để tính BMI.")


# 5. Nhập số giây, chuyển sang giờ:phút:giây (Thử thách)
# Ví dụ: 3661 giây → "1 giờ 1 phút 1 giây"
so_giay = int(input("Nhập số giây: "))
gio = so_giay // 3600
phut = (so_giay % 3600) // 60
giay_con_lai = so_giay % 60
print(f"{gio} giờ {phut} phút {giay_con_lai} giây")

