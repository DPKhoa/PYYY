#print('Kteam', 'python',end='???')
'''from time import sleep 
print('start...',end=" ")#k còn newline nên sẽ đợi đến khi có newline sẽ xuất
sleep(3)
print('end....')'''
'''with open('printtext.txt', 'w') as f:
		print('printed by print function',file=f)
'''
'''from time import sleep # nhập hàm sleep từ thư viện time

print('line 1\n', 'line2', end='')
sleep(3) # dừng chương trình 3 giây
print('end...')
'''
'''from time import sleep # nhập hàm sleep từ thư viện time

print('line 1', 'lin\ne2', end='')
sleep(3) # dừng chương trình 3 giây
print('end...')

from time import sleep # nhập hàm sleep từ thư viện time

print('start...', end='', flush=True)# nếu là true nó sẽ yêu cầu xuất ra những gì trong bộ nhớ đệm
sleep(3) # dừng chương trình 3 giây
print('end...')
'''
'''from time import sleep

your_name = "Henry"
your_great = "Hello! My name is "

for c in your_great + your_name:
    print(c, end='', flush=True)
    sleep(0.1)
print()
'''
chuoi = [('bố','mẹ','em')]
print(type(chuoi))
tup = [1, 2]
print(type(tup))
tup += ('how', 'kteam')
print(tup)
print(type(tup))