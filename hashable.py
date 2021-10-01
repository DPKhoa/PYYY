# hàm id kq trả về sẽ là int or longint là hằng số 
#với số nguyên k dổi chuỗi sẽ đổi
'''a = id('Kteam')
c = id((1,2,3),)
print(a)
print(c)
n = 69
print(n)
print(n * 2)#print(1+n)
print(n.__mul__(2))#print(n.__radd__(1))
'''
'''s_1 = "HowKteam"
s_2 = 'Free education'
s_1 = s_1 + 'python'
s_2 +='python'
print(id(s_1))
print(id(s_2))'''
s_1 = [1,2]# hash object
s_2 = [3,4]
print(id(s_1))
print(id(s_2))
s_1 = s_1 +[0]
s_2 += [0]
print(id(s_1))
print(id(s_2))