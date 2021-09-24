'''a = [1,2,3,4]
c = a.count(1)#số lần xuất hiện trong list 
print(c)'''
	#a.index(1) giống chuỗi
'''a = [1,2,3,4]
c = a.copy()
print(a)
print(c)
c[0] = 'kteam'
c = a.clear()
print(a)
print(c)'''

'''a = [1,2,3,4]
a.append(5)#them vao list
print(a)
a.append([5,6])#them vao voi 1 phan tu list
print(a)
a.extend([7,8,[9,10]])# mo rong va lay tung tu phan tu vao list
print(a)
a.insert(-1,821)#them vao gia tri theo vi tri
print(a)'''

'''a = [1,2,3,4]
print(a)
c = a.pop(1)# lay ra gia tri
print(a)
print(c)''' 

'''a = [1,2,3,4]
c = a.remove(1)
print(c)'''

'''print(a)
a.reverse()
print(a)'''
#print(a)
#a.sort(reverse=True)
#Sap xep xem co dao chieu hay k Reserve=True se dao chieu va nguoc lai
#sap xep lai thu tu cung kieu du lieu
#print(a)
a = [[1, 2], ['abc', 'def']]
a.sort()
print(a)