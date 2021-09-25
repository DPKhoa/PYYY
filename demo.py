# gán cho biến a giá trị là 4 .VỚi 4 là số nguyên 
'''a = 4 
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
print(com.imag)'''

import math   # lấy nội dung của thư viện math về sử dụng
math.trunc(3.9)
'''math.fabs(-3)
 math.sqrt(16)
 math.gcd(6, 4)'''

'''a = 8
b = 3
a + b   # tương đương 8 cộng 3

a – b    # tương đương 8 trừ 3

a * b   # tương đương 8 nhân 3

a / b   # tương đương 8 chia 3

a // b  # tương đương với 8 chia nguyên 3

a % b   # tương đương với 8 chia dư 3

a ** b   # tương đương 8 mũ 3'''

