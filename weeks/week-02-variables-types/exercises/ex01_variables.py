"""Bài tập 01: Biến trong Python 📦
=================================
Mục tiêu: Hiểu cách khai báo và sử dụng biến
"""

# 1. Tạo 4 biến lưu thông tin cá nhân
ten = "An"  # str
tuoi = 18  # int
diem_tb = 8.5  # float
dang_hoc = True  # bool

print("Tên:", ten, "- Kiểu dữ liệu:", type(ten))
print("Tuổi:", tuoi, "- Kiểu dữ liệu:", type(tuoi))
print("Điểm trung bình:", diem_tb, "- Kiểu dữ liệu:", type(diem_tb))
print("Đang học:", dang_hoc, "- Kiểu dữ liệu:", type(dang_hoc))

# 2. Hoán đổi giá trị 2 biến KHÔNG dùng biến tạm
a = 10
b = 20
a, b = b, a
print("Sau khi hoán đổi: a =", a, ", b =", b)

# 3. Augmented assignment
# Cho x = 100. Dùng +=, -=, *=, //= để biến đổi x qua 4 bước
x = 100
x += 10
print("Sau += 10:", x)
x -= 20
print("Sau -= 20:", x)
x *= 2
print("Sau *= 2:", x)
x //= 3
print("Sau //= 3:", x)

# 4. Multiple assignment (Thử thách)
ho, ten, tuoi = "Nguyễn", "An", 18
print(f"Họ tên: {ho} {ten}, {tuoi} tuổi")

