file_object = open('Kteam.txt')
'''data = file_object.readlines()# mỗi phần tử là 1 dòng dạng list có escape sequen
data2 =file_object.readline()
#khi đọc con trỏ sẽ trỏ đến cuối file cho nên k thể đọc tiếp 
# nếu muốn đọc thì dùng phương thức close rồi open lại
'''
'''data = tuple(file_object)# có thêm list
file_object.close()'''
#data =file_object.write('K2')#mode='w' xóa hết nội dung cũ
data = file_object.read()
file_object.seek(50)# trả về index ma ban muon
data2=file_object.read()
file_object.close()
print(data)
print(data2)

teo_file = open('teo.txt', 'w+')
teo_file.write('Teo dep trai\n')
teo_file.read()

