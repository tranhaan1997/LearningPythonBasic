lst = []
while True:
    num = input("nhập số tự nhiên vào đây(nhập phím bất kỳ khác số tự nhiên để dừng lại): ")
    if num.isdigit():
        lst.append(int(num))
    else:
        print("stop!!!. Vì nó không phải số tự nhiên...")
        break
tong = sum(lst)#tính tổng
print("Danh sách các số tự nhiên vừa nhập\n",lst)
print("Tổng = ",tong)
x= int(input("Nhập x: ")) #tính số lần xuất hiện
if x in lst:
    solan = lst.count(x)
    print(f"số {x} xuất hiện trong list {solan} lần")
else:
   print(f"{x} không có xuất hiện trong list")
#tìm lớn hơn x
if x > max(lst):
    print(f"{x} lớn hơn tất cả các số trong list")
else:
    print(f"số {x} không phải là số lớn nhất")
lst2= []
for num in lst:  #tính list nhỏ hơn x
    if num > x:
        lst2.append(num)
print("các con số lớn hơn x là: ",lst2)
