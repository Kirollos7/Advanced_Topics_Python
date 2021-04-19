d = "I'am a programmer"
print(d)
# print(d[::-1])


# a = """Hello
# world all is will be 
# done.
# """
# # print(a)
# h = 'Hello'
# name = 'Kirollos'
# print(h + ' ' + name)
# print('#' * 49)
# print('\n\n\n\n')

# if 'Iam' in d:
#     print('done')
# else:
#     print('no')



# k = 'Hello World!'
# k = k.strip()
# # strip ----> Remove spaces
# print(k.count('o'))
# print(k.count('l'))
# print(k.count('w'))

# nn = k.replace('world', 'Egypt')
# print(nn)














print('#' * 49)
print('\n\n\n\n')


# VIP
my_string = 'how,old,are,you'
my_list = my_string.split(",")
print(my_list)
print(len(my_list))

print('/' * 49)

# Very Important Method
new_string = ' '.join(my_list)
print(new_string)


# Very Important Method join convert from list to string
l = [ 'name' , 'help']
tt = ' '.join(l)
print(tt)










from sys import getsizeof
from timeit import default_timer as timer

# Good Code
new_list = list(['Apple', 'Microsoft', 'Facebook', 'IBM'])
start = timer()
company = ' '.join(new_list)
end = timer()
print('Join Time = ' , end - start)

# Bad Code
s = timer()
c = ''
for i in new_list:
    c += i
    c += ' '
e = timer()
print('for  Time = ' , e - s)


print('*' * 49)
print(company)
print(c)
print('r' * 49)

print(getsizeof(company), 'bytes')
print(getsizeof(c), 'bytes')




# formating string

name = input('Enter name : ')
age = int(input('Enter Age : '))

print(f'Welcome {name} , you are {age}')