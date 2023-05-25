# lst = []
# while True:
#     num = input("nhập số tự nhiên vào đây(nhập phím bất kỳ khác số tự nhiên để dừng lại): ")
#     if num.isdigit():
#         lst.append(int(num))
#     else:
#         print("stop!!!. Vì nó không phải số tự nhiên...")
#         break
# tong = sum(lst)#tính tổng
# print("Danh sách các số tự nhiên vừa nhập\n",lst)
# print("Tổng = ",tong)
# x= int(input("Nhập x: ")) #tính số lần xuất hiện
# if x in lst:
#     solan = lst.count(x)
#     print(f"số {x} xuất hiện trong list {solan} lần")
# else:
#    print(f"{x} không có xuất hiện trong list")
# #tìm lớn hơn x
# if x > max(lst):
#     print(f"{x} lớn hơn tất cả các số trong list")
# else:
#     print(f"số {x} không phải là số lớn nhất")
# lst2= []
# for num in lst:  #tính list nhỏ hơn x
#     if num > x:
#         lst2.append(num)
# print("các con số lớn hơn x là: ",lst2)

kt = 1
kt2 = "y"
dssv = {}
fnd = {}
while kt:
    print('Nhập thông tin danh sách sinh viên!!!')
    manv = (input('Nhập mã sinh viên: '))
    tensv = (input('Nhập tên sinh viên: '))
    diemso = (eval(input('Nhập điểm số: ')))
    namsinh = (int(input('Nhập năm sinh: ')))
    kt = (int(input('nhập giá trị tiếp không:  1:có   0:không : ')))
    dssv[manv] = [tensv,diemso,namsinh]
    if kt == 0 :
        break
    elif kt !=1:
        print('vui lòng kiểm tra lại cú pháp')
print("Danh sách sinh viên \n")
print(dssv)
def tim(find):
    if find not in dssv:
        return "Không tìm thấy trong dssv"
    else:
        tim = [tensv,diemso,namsinh]
        return tim
while kt2:
    tim_MSV = input("Nhập mã sinh viên cần tìm: ")
    fnd = tim(tim_MSV)
    print(fnd)
    kt2 = input("Nhấn y để tiếp tục hoặc nhấn bất kỳ để dừng lại!!!   ")
    if kt2 =="n":
        break
    else:
        kt= input("Bạn muốn tiêp tục hay không(y/n): ")