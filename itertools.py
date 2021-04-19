# Iter Tools: product, permutations, combinations, accumulate, group by and infinite iterators

from itertools import count , cycle, repeat, groupby ,accumulate , combinations_with_replacement, combinations, product, permutations
import operator

# infinite
# count , cycle, repeat

a = [1,2,3,4]
for i in repeat(1, 10):
    print(i)























# persons = [
#     {'name': 'Tim', 'age' : 25},
#     {'name': 'Sam', 'age' : 99},
#     {'name': 'John', 'age' : 30},
#     {'name': 'Kyrollos', 'age' : 22},
# ]
# group_obj = groupby(persons, key=lambda x: x['age'])

# for key, value in group_obj:
#     print(key,' | ',list(value))



























# is a جمع accumulate 
# acc = accumulate(a, func=max)
# print(a)
# print(list(acc))













# comb = combinations(a, 2)
# print(list(comb))

# print('*' * 49)
# co = combinations_with_replacement(a, 2 )
# print(list(co))







# perm = permutations(a)
# print(list(perm))

# b = ['Kirollos', 'Mina',]
# products = product(a,b, repeat=2)
# print(list(products))




