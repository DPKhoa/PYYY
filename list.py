'''a = list('Khoa')
print(a)
a = [[n,n*2,n*3] for n in range(1,4)]
print(a)
a = [1,2]
a += ['one', 'two']#k thể nhân 2 list chuỗi vs nhau 
b = 1 in a
print(b)
a = [1,2,'a','b','c',[3,4]]
a[1] = 'Kteam'
b = a[1]
print(b)
print(a)'''
a = [[1,2,3],[4,5,6],[7,8,9]]
print(a[0][-1])
a = [1,2,3]
#giúp tạo ra giá trị riêng cho b
b = list(a)
b[0] = 'Kteam'
print(a)
print(b)
a = 'aaaaaaaAAAAAaaa//123123//000000//&&TTT%%abcxyznontqfadf'
b = a.lstrip('aaaaaaaAAAAAaaa//123123//000000//&&')
c = b.rstrip('%%abcxyznontqfadf')
print(c)

print(a.partition("TTT")[1])# lấy giá trị index thứ 1
#code = a.split('&&')[-1].split('%%')[0]
