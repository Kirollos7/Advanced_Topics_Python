# map function transforms each element with function

''' 
    Words
# function argument paramenter
def max_value(argument1 , argument2):
    return argument1

max_value(paramenter1 , paramenter2)

'''

# lambda arguments : expression
# map(func, sequence)
# filter(func, sequence)
# reduce(func, sequence) 
# sequence meaning list
from functools import reduce

my_list = [ 5, 6]
product = reduce(lambda x,y : x*y, my_list)
print(product)

print('#' * 70)
# 01222208220


# filter
b = filter(lambda x: x%2==0, my_list)
print(list(b))

# list comprehention
l = [o for o in my_list if o%2==0]
print(l)




# map
multi_each_element_by_2 = map(lambda x : x*3, my_list)
convert_map_object_to_list = list(multi_each_element_by_2)
print(convert_map_object_to_list)

# list comprehention
k = [x*3 for x in my_list]
print(k)






# point2D = [(1, 2), (15, 1), (5, -1), (10, 4)]

# def sort_by_y(a):
#     return a[1]

# point2D_sorted = sorted(point2D, key= lambda x : x[0] + x[1])
# point2D_sorted_y = sorted(point2D, key=sort_by_y)

# print(point2D)
# print(point2D_sorted)
# print('*' * 60)
# print(point2D_sorted_y)










# add10 = lambda x : x+10
# print(add10(20))

