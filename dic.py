#dic{key:value}
'''dic = {'name': 'Kteam', 'member':69}
print(type(dic))
dic = {}==dic = dic()
print(dic)
'''
'''
dic = {key: value for key, value in [('name','Kteam'),('member',69)]}
print(dic)

iter = [('name', 'Kteam')]
dic = dict(iter)
 
dic = dict(Kteam='HowKteam' , FE='Free education')
print(dic)
'''
'''iter_ = ('name' , 'number', 69, True)
dic = dict.fromkeys(iter_,'Khoa')
print(dic)
dic['aaaa'] = 'Free education'#tự động thêm 1 phần tử vào
print(dic)
print(dic['name'])'''
dic = dict(k='Kteam', HK='HowKteam', FE='Free education')
dic['k'] = dic['k'] + ' - Share tobe better'
print(dic)
