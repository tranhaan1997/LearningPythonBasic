# Bài 1

# don_gia = eval(input("Vui lòng nhập đơn giá: "))
# so_luong = eval(input("Vui lòng nhập số lượng: "))
# print("thành tiền là: {:,.1f}" .format(don_gia*so_luong))

#Bài 2

# do_c = eval(input("Nhập vào độ C: "))
# do_f = 9/5 * do_c + 32
# print("Nhiệt độ C = %.2f thì độ F = %.2f" %(do_c, do_f))

# Bài 3

# chuoi = input("Nhập chuỗi: ")
# print("Chuỗi '%s' có chiều dài: " %chuoi, len(chuoi))
# nhap_in = eval(input("Nhập vào index: "))
# print("Ký tự tại vị trí index %d là: " %nhap_in, chuoi[nhap_in])
# ran_dau, ran_cuoi = input("Nhập range index để lấy ký tự: ").split(",")
# print("Ký tự từ vị trí index %s đến %s là: " %(ran_dau,ran_cuoi), chuoi[int(ran_dau):int(ran_cuoi)])

# Bài 4

# lai_suat = eval(input("Nhập lãi xuất 1 năm (%): "))
# tien_gui = eval(input("Nhập số tiền gửi: "))
# thang_gui = eval(input("Nhập số tháng gửi: "))
# tien_lai = (tien_gui * thang_gui) * (lai_suat/12/100)
# tong_tien = tien_gui + tien_lai
# print('Tiền lãi: {:,.2f}'.format(tien_lai))
# print('Tổng tiền: {:,.2f}'.format(tong_tien))
