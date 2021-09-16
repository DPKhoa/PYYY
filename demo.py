# gán cho biến a giá trị là 4 .VỚi 4 là số nguyên 
a = 4 
print(a)
#kiểu dữ của a
print(type(a))

# lấy toàn bộ nội dung của thư viện decimal

from decimal import*
#lấy tối đa 30 phần tử của decimal và phần thập phân của Decimal

getcontext().prec = 30
#chỉ cần 1 thằng là Decimal cả biểu thức sẽ là Decimal
d = Decimal(10)/Decimal(3)
print(d)
print(type(d))
f = 10/3
print(f)
print(type(f))

#phân số 
from fractions import*
frac = Fraction(6,9)
frac1 = Fraction(5,10)
frac2 = frac + frac1
print(frac)
print(type(frac))
print(frac2)

#<phẩn thực>+<phần ảo>j
com=complex(2,5)
print(com)
print(com.real)
print(com.imag)
