# Sets: is a collection datatype unordered, mutable, No duplicates of element
# all element is unique


# s = set([1,2,3,4,5])

# print(s)

ss = set()
ss.add(45)
ss.add(4)
ss.add(5)

ss.remove(4)
# remove
ss.discard(4554)


# print(ss.pop())

ss.add(545)
ss.add(100)
ss.add(20)
ss.add(80)
# print(ss)
# print(type(ss))




odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}


# u = odds.union(evens)
# print(u)


# i = odds.intersection(primes)
# print(i)

# i2 = evens.intersection(primes)
# print(i2)

a = {1,2,3,4,5,6}
b = {1,2,3}

r = a.difference(b)
print(r)

r2 = b.difference(a)
print(r2)

print('*' , 50)

semantic1 = a.symmetric_difference(b)
print(semantic1)

semantic2 = b.symmetric_difference(a)
print(semantic2)


print('/' * 49)
print('/' * 49)
print('/' * 49)
print('/' * 49)
print('/' * 49)
print('/' * 49)
print('\a\n\n\n')

my_set = {1,2,3,4,5,6}
# any change in any set will effective on both of them
my_set2 = my_set

s = my_set.copy()
print(s)
print(my_set)

s.add('Mina')
print(s)
print(my_set)

# print(my_set)
# print(my_set2)

# my_set.add(101)
# my_set2.add(45)


# print(my_set)
# print(my_set2)







print('/' * 49)
print('/' * 49)
print('/' * 49)
print('/' * 49)
print('/' * 49)
print('/' * 49)
print('\a\n\n\n')



# frozen Set can`t change anything or delete or do anythong in this set
kk = frozenset([1,2,3,4,5])
print(kk)

for i in kk:
    print(i)
