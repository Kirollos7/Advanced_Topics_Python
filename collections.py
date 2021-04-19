# collections: Counter, namedtuple, Ordered Direct, 
from collections import Counter, namedtuple, defaultdict, deque

s = 'I\'m a Programmer'
print(s)
# Counter is a dictionary values
# my_counter = Counter(s)
# print(my_counter.keys())
# print(my_counter.values())
# print(my_counter.items())
# print(my_counter.most_common(2))
# print(my_counter.most_common(2)[0][0])
# print(list(my_counter.elements()))




# stract
# Class
Point = namedtuple('Point', 'x,y')
# pt is a object from Point Class
pt = Point(4,10)
print(pt.x, pt.y)



d = defaultdict(int)
d['a'] = 1
d['b'] = 3
d['c'] = 5
d['d'] = 7
d['e'] = 9
d[100] = 'f'

print(d)




# Itertools