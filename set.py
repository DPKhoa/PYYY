'''set_1 = {65,66}
print(set_1)
print(type(set_1))

set_2 ={'HowKteam','Kteam',69}#?
print(set_2)

set_3 ={(69, 'Free education'),(1,2,3)}
print(set_3)
'''
#set_4 = {[1,2], [3,4]}
#print(set_4)
# k thể tạo ra emty set hoặc một set trong đó hoặc dữ liệu unhash
'''set_5 = set((1,2,3))
print(set_5)
#k quan tâm theo thứ tự 
set_6 = set('HowKteam')
print(set_6)
print(type(set_6))
# có thể tạo một empty set 
'''
#Venn
print(1 in{1,2,3}) # k thể kt 1 set nằm trong set
print((1,2)in {(1,2),3})

print({1,2,3}-{2,3})# kết quả chỉ tồn tại trong set 1 và không tồn tại trong set 2
print({1,2,3} & {2,3})# toản tử  hoặc lấy hết |
print({1,2,3}^{2,3})# lấy hết hai bên và chỉ lấy phần từ k trùng
#.clear() xóa hết các phần tử trong set 
#.pop() lấy ra thằng đầu tiên,nếu là rỗng thì sẽ báo lỗi 
#/remove(N) N:remove số bạn muốn ,nếu remove một thằng k tồn tại trong set sẽ báo lỗi 
#.discard(N) N:giống thằng trên nhưng remove thằng k có sẽ k báo lỗi
#.copy():
#.add(N):add thêm 1 phần tử vào 

set1 = {1,2,3,4}
'''print(id(set1))
set1.add(5)
print(id(set1))'''
print(set1)
set2 = set1
print(set2)
set2.clear()
print(set2)
