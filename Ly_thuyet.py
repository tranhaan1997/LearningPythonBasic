# print("**  **  ****** **    **     ******")
# print("**  **  **     **    **     **  **")
# print("******  ****** **    **     **  **")
# print("**  **  **     **    **     **  **")
# print("**  **  ****** ****  ****   ******")


# a, a1 = 4,5
# print(a,a1)

# b, pi = 4, 3.14
# print("b = %d là số nguyên và pi = %.2f là số thực" % (b,pi))


# c = 5,4,2,3,1
# print(c)

# print(type(c))

# d = 1, 'hello', 3.14
# print(type(d))

# result = True
# print(result)
# print(type(result))

# not_result = not result
# print(not_result)
# print(type(not_result))


# hello = """
# **  **  ******  **    **      ******
# **  **  **      **    **      **  **
# ******  ******  **    **      **  **
# **  **  **      **    **      **  **
# **  **  ******  ***** *****   ******
# """
# print(hello)
# print(type(hello))

# hi = 'hello world'
# print(hi[0])
# print(hi[0 : 5]) # Mặc định from : index và to : index + 1 
# print(hi[:5])
# print(hi[-5:])
# print(len(hi))


# chuoi_1 = 'hello'
# chuoi_2 = "world"

# print(chuoi_1 + ' ' + chuoi_2)
# print((chuoi_1 + ' ') * 3)


# a = '10'
# b = 5

# print(int(a) + b)


# a = '10 + 10.5'
# b = eval(a)
# print(b)
# print(type(b))


# print(chr(98))

# a = 4
# b = 5
# c = 1
# print("tong cua 3 so abc = %d va tich cua 3 so abc = %d" %(a+b+c,a*b*c))
# print("tong cua 3 so %d + %d + %d = %d" %(a,b,c,a+b+c))

# a = 3.14545656
# print("%10.2f" %(a))

# b = 'hello world'
# print('%.5s' %(b)) 


# a = "tâm"
# b = 'python'
# print('trung %s tin học'  %(a) + ' abc %s' %(b))
# print('%s' %(a))
# print("khoa hoc" + " python")

# a,b = 5 , -7
# print('{} + {} = {}'.format(a,b,a+b))
# print('{x} + {y} = {z}'.format(x=a,y=b,z=a+b))
# print('{:+.2f} {:+.1f} = {:+.1f}'.format(a,b,a+b))
# print('{:0>5d} + {:<6d} = {:>2d}'.format(a,b,a+b))

# n = 122345566778
# print('{:,.1f}'.format(n))


# b = 100
# print('{:,.1f} cm\u00b2'.format(b))

# print('what\n your name?')
# print('What\'s your name?')

# name = input("what is your name: ")
# print("your name is: %s" %name)
# print("your name is:", name)

# a = eval(input("Nhập vào số a: "))
# b = eval(input("Nhập vào số b: "))
# c = eval(input("Nhập vào số c: "))
# print("%d + %d + %d = %d" %(a,b,c,a+b+c))


# mat_khau = input("Nhập mật khẩu: ")
# if mat_khau == "anth":
#     print("Mật khẩu chính xác")
# else:
#     print("Sai mật khẩu")
    
# mat_khau = input("Nhập mật khẩu: ")
# if mat_khau != "anth":
#     print("Nhập sai mật khẩu")
# else:
#     print("Nhập đúng mật khẩu")

# so = int(input("Nhập vào số nguyên: "))
# if so >= 0:
#     if so == 0:
#         print("Là số 0: ",so)
#     else:
#         print("Là số nguyên dương:", so)
# else:
#     print("Là số nguyên âm: ",so)

# a = eval(input("Nhập x: "))
# if a >= 0:
#     print("Giá trị tuyệt đối của x là: ",a)
# else:
#     a = -a
#     print("Giá trị tuyệt đối x là: ",a)

# Vòng lặp while
# i = 1
# while i <=  10:
#     print(i)
#     i += 1


# n = 1
# while n == 1:
#     print("thoa dk")
#     n = eval(input("Nhâp n: "))

# print("Bảng cửu chương 2")
# i = 1
# while i <= 10:
#     print("3 x ",i," = ",3*i)
#     i += 1


# In ra số thứ tự từ 10 đến 1
# a = eval(input("Nhập vào số nguyên: "))
# while a >= 1:
#     print(a)    
#     a -= 1
# print("start!!!")

# Tính tổng các số nguyên nhập vào
# print("Chương trình tính tổng N số nguyên")
# a = int(input("Nhập n: "))
# b = 1
# tong = 0
# while b <= a:
#     c = int(input("Nhập vào số nguyên thứ %d: " %(b)))
#     b += 1
#     tong += c
# print ("Tổng = ", tong)

# In một dãy số
# dayso = [1,2,3,4,5,9,8,7,6]
# for so in dayso:
#     print("Cac so la: ",so)
    
# In phần tử trong chuỗi
# chuoi = "Hello world!"
# for kytu in chuoi:
#     print("Ký tự là: ",kytu)

# Tạo ra một dãy số
# print("Tạo ra dãy số: ",list(range(10,1,-1)))
# print("Tạo ra dãy số: ",list(range(1,10,2)))

# Áp dụng range vào trong vòng for
# for i in range(1,11):
#     print("3 x ",i," = ",3*i)
    
# for i in range(10,0,-1):
#     print("3 x ",i," = ",3*i)


# Cho người dùng nhập vào một chuỗi. Đếm số ký tự trắng có trong chuỗi
# chuoi = input("Nhập vào một chuỗi: ")
# i = 0
# dem = 0
# while i < len(chuoi):
#     if chuoi[i] == " ":
#         dem += 1
#     i += 1
# else:
#     print("Chuỗi có số khoảng trắng là: ",dem)


# Cho người dùng nhập vào n số nguyên. Tính trung bình cộng của các số nguyên
# so = int(input("Bạn muốn nhập bao nhiêu giá trị: "))
# tong = 0
# for i in range(1,so+1):
#     gia_tri = int(input(f'Nhập vào giá trị {i}: '))
#     tong += gia_tri
# else:
#     print(f'Giá trị trung bình: {tong/so}')


# # Thực hành lệnh break
# danh_sach_so = [1,2,3,4,5,6,7,8,9]
# gia_tri_tim = int(input("Nhập vào giá trị cần tìm: "))
# n = 0
# while n < len(danh_sach_so) - 1:
#     if danh_sach_so[n] == gia_tri_tim:
#         print(f'Tìm thấy giá trị {gia_tri_tim} tại vị trí index = {n}')
#         break
#     n += 1
# else:
#     print(f'Không tìm thấy giá trị {gia_tri_tim} trong danh sách')


# Các kiểu khai báo in ra màn hình
# a,b = 1,2

# print("giá trị a = %d  và b = %d" %(a,b))
# print("Giá trị của a = {} và b = {}" .format(a,b))
# print (f'giá trị a = {a} và b = {b}')

# in ra những tên ngoại trừ tên có 4 chữ
# danh_sach_ten = ['mai', 'cúc','trúc','đào','đông','xuân','hạ','thu']
# for ten in danh_sach_ten:
#     if len(ten) == 4:
#         continue
#     print('Xin chào', ten)
# print('kết thúc')

i = 1
while i:
    nhap_chuoi = input("Nhập vào ký tự: ")
    if nhap_chuoi == "0":
        break
    i += 1