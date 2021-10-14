'''set_ = {5, 8, 1, 9, 4}
sum = 0
for i in set_:
	print(iset_ = {5, 8, 1, 9, 4})
	sum += i
print(sum)
'''
'''k = range(3)
print(k)
print(list(range(2,-3,-1)))# stop -step 
'''
'''lst = [5, (1,2,3), {'abc','xyz'}]
for i in range(len(lst)):
	print(lst[i])
'''
'''lst = [1,2,3]
for value in lst:
	value+=1
print(lst)'''	
'''lst = [1,2,3]
for value in range(len(lst)):
	lst[value]+=1
print(lst)
'''
'''lst = ['--'.join((a.capitalize(), b.upper() + c.lower())) for a, b, c in [('how', 'kteam', 'EDUCATION'), ('chia', 'sẻ', 'FREE')]] # bỏ trống optional-predicate
print(lst)'''
'''lst = []
for a,b,c in [('how', 'kteam', 'EDUCATION'), ('chia', 'sẻ', 'FREE')]:
	a = a.capitalize()
	b = b.upper()
	c = c.lower()
	lst.append('--'.join((a,b+c)))
print(lst)
'''
'''student_list = ['Long', 'Giàu', 'Trung', 'Thành']
for idx ,student in enumerate(student_list,100):
	print(idx, '=>', student)
'''
lst = [[1, 2, 3], [4, 5, 6]]
lst = [[1, 2, 3], [4, 5, 6]]

for x in lst:

    x[0] = None

print (lst)