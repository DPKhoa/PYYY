'''a = 'How Kteam free education'
#b = a.rsplit(' ',2)#rsplit,lsplit
print(b)'''
#cắt chuỗi trước và sau chữ K
a = 'How Kteam free education'
b = a.isspace()

#b = a.partition('t')#rpartition
#b = a.rpartition('free')#cắt từ phải
print(b)
'''
#tìm số lượng chữ e từ vị trí 0 đến vị trí 10 
b = a.count('e',0,10)
b = a.startswith('How',4,9)#vị trí 0 đến vị trí 10
#b = a.endwith() 
b = a.find('Kteam')#tìm vị trí có find,còn tìm k thấy sẽ quăng ra -1
#b = a.index('y')# nếu tìm k thấy sẽ quăng ra lỗi 
b = a.islower()#isupper
b = a.isdigit()# kiểm tra có phải là số không 
b = a.isspace( )
#print(a)
#print(b)
s = 'aaaAAaaaooaa neu mot Ngay naO Doaaaaaaa'
d = s.lstrip('aaaAAaaaooaa')
k = d.rstrip('aaaaaaa')
h = k.replace('O','o')
q = h.title()# viết hoa các chữ cái đầu dòng
print('aaaAAaaaooaaneu mot Ngay na0 Doaaaaaaa'.strip('aA').lstrip('ao').title().replace('0','o'))'''
