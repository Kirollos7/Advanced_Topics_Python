# Dictionary: Key-Value pairs, Unordered, Mutable
# Maps

# Deleteing Form Dict
# delete from dictionary ----> dict.pop('<Key Name>')
# or using
# delete from dictionary ----> del dict('<Key Name>')
# or using
# dict.popitem()

d = {'name' : 'Kirollos', 'age' : 21, 'city' : 'Cairo'}
d2 = dict(name='Samy', age=40, address='5-ST Omar', code=105)
print('Dict1', d)
print('Dict2', d2)

d2.update(d)
print('Dict#', d2)



# for key,value in d.items():
#     print(key + ':' + value)

# print('*' * 50)
# for value in d.values():
#     print(value)

# print('*' * 50)






print('*' * 50)


try:
    print('My name is : ' ,d['name'])
except:
    print('Error')

# if 'name' and 'age' in d:
#     print('my name is : ', d['name'], '\a\nand my age is : ', d['age'])
# else:
#     print('Sorry Your data not allowed')



print('+' * 50)


oo = {1 : 10 , 2 : 20, 3 : 30, 4 : 30, 4 : 40}
print(oo)
for key,value in oo.items():
    print(key , ':', value)

print('+' * 50)


m = [8 , 7]

pp = {'mm': m}
print(pp)

for i, j in pp.items():
    for k in j:
        print(k+100)
    print(i,j)

# VIP Note
'''
The Key in Dictionary may be a Tuple Due To : tuple is a immutable Data Structure
Impossible Key == List No Due to List is mutable Data Structure
'''





# d['email'] = 'kirollosnoshi@gmail.com'
# d['name'] = 'Noshy'
# d['Address'] = '11-ST'

# print('*' * 50)
# print(d)
# del d['email']
# print(d)
# print('*' * 50)
# # Or
# d.pop('age')
# print('*' * 50)
# print(d)
# print('*' * 50)


# print(d)
# print('*' * 50)

# d.popitem()
# print(d)







# my_dict = dict(name="Shad", age=20, address='All')
# print(my_dict)
