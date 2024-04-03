''' 
Đọc 1 file văn bản gồm nhiều dòng
Ghi ra màn hình theo thứ tự ngược lại của các dòng


 '''
# Mở file văn bản để đọc
with open("TrinhNgocTanText.txt", "r") as file:
    # Đọc tất cả các dòng từ file và lưu vào danh sách lines
    lines = file.readlines()

# In các dòng theo thứ tự ngược lại
for line in reversed(lines):
    print(line.strip())  # Sử dụng strip() để loại bỏ kí tự xuống dòng thừa