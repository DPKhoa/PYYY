'''k =5 
while k > 0:
	print('k =',k)
	k -= 1
'''
'''
s = 'HowKteamo'
idx = 0
length = len(s)
while idx < length:
	print(idx, 'stands for', s[idx])
	idx += 1
'''
five_even_numbers = []
print(type(five_even_numbers))
'''k_number = 1
while True:
	if k_number % 2 == 0:
		five_even_numbers.append(k_number)
		if len(five_even_numbers) >= 5:
			break
	k_number += 1
print(five_even_numbers)
print(k_number)
'''
'''k_number = 0
while k_number < 10:
	k_number += 1
	if k_number % 2 == 0:
		continue
	print(k_number, 'is odd number')
print(k_number)
'''
'''k = 0 
while k < 3:
	print('value of k is ', k)
	k+=1
	if k==1:
		break;
else:
	print('k is not less than 3 anymore')
'''

# bài 2
with open('draft.txt') as f:
    # lấy nội dung của file dưới dạng một list
    data = f.readlines()
idx = 0 # mốc bắt đầu
length = len(data) # mốc kết thúc
new_content = '' # nội dung mới sẽ ghi vào file mới

while idx < length:
    # tách một dòng thành một list
    line_list = data[idx].split()
    # print(line_list)
    idline = 0
    length_line = len(line_list)
    while idline < length_line:
        if line_list[idline] == 'Kteam':
            # thay thế chữ trước Kteam là How
            line_list[idline - 1] = 'How'
            #print(line_list)
        idline += 1
    # nối lại thành một dòng chuỗi
    new_content += ' '.join(line_list) + '\n'
    print(new_content)
    idx += 1

with open('kteam.txt', 'w') as new_f:
    # ghi nội dung mới vào file kteam.txt
    new_f.write(new_content)
    
# bài 3
'''#C1
lst = [56, 14, 11, 756, 34, 90, 11, 11, 65, 0, 11, 35]
idx = 0
maidx = len(lst) - 1
majdx = len(lst)

while idx < maidx:
    if lst[idx] == 11:
        idx += 1
        continue
    jdx = idx + 1
    while jdx < majdx:
        if lst[jdx] == 11:
            jdx += 1
            continue
        if lst[idx] > lst[jdx]:
            lst[idx], lst[jdx] = lst[jdx], lst[idx]
        jdx += 1
    idx += 1
print(lst)
'''
'''a = [56, 14, 11, 756, 34, 90, 11, 11, 65, 0, 11, 35]

# Loại bỏ các số 11
b = [i for i in a if i!=11]

# Lưu lại các vị trí của số 11
c = [i for i in range(len(a)) if a[i]==11]   # vị trí của các số 11: 2,6,7,10

# Sắp xếp lại list đã bỏ 11 theo thứ từ từ bé đến lớn
b.sort()

# Dùng phương thức insert của list với các vị trí của số 11 đã lưu
for j in c:
    b.insert(j,11)
print(b)
'''