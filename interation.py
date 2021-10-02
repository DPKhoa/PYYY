itera = (x for x in range(3))#generator object
print(itera)
#print(next(itera))#truy xuất nó bằng cách lấy ra từng phần tử
#print(next(itera))
#print(sum(itera,2)) #0+1+2=3 +2 =5
# k next sau khi sum
print(max(itera,default='Kteam'))