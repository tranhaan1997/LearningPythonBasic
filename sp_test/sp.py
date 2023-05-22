import speedtest, math

def bytes_to_mb(size_bytes):
    i = int(math.floor(math.log(size_bytes, 1024)))
    power = math.pow(1024, i)
    size = round(size_bytes / power, 2)
    return f"{size} Mpbs"

wifi = speedtest.Speedtest()

print("Đang kiểm tra tốc độ download... ")
download_speed = wifi.download()

print("Đang kiểm tra tốc độ upload... ")
upload_speed = wifi.upload()

print("Download: ", bytes_to_mb(download_speed))
print("Upload: ", bytes_to_mb(upload_speed))

# from datetime import datetime
# try:
#     date_string = input("Nhập theo định dạng (dd/mm/yyyy): ")
#     date_obj = datetime.strptime(date_string, "%d/%m/%Y, %H:%M:%S").strftime("%d/%m/%Y, %H:%M:%S")
#     # print("Chuỗi đã nhập:", date_string)
#     print("datetime(DD/MM/YY): ", date_obj)
# except:
#     print("Ngày không hợp lệ!")
    
    