
# def spin_words(sentence):
#     # Your code goes here
#     n = []
#     s = sentence.split(' ')
#     for i in s:
#         if len(i) >=5:
#             i[::-1]
#             # n.append(g)
#         # else:
#             # n.append(i)
#         # f = ' '.join(n)
#     return s

# print(spin_words('Kirollos Noshy B all'))




# def to_weird_case(string):
#     s = string.split(" ")
#     n = []
#     # r = [] 
#     for i in s:
#         for idx, val in enumerate(i):
#             if idx%2 == 0:
#                 s1 = val.upper()
#                 n.append(s1)
#             else:
#                 n.append(val)
#         n.append(' ')
#         r = ''.join(n)
#     return r

   


# print(to_weird_case("Weird string case"))
# print(to_weird_case("string"))
# print(to_weird_case("ThIs"))




# a = int(input())
# b = int(input())
# c = int(input())
# m = max(a,b,c)
# if m == a:
#     print(1)
# elif m == b:
#     print(2)
# else:
#     print(3)


a = int(input())
b = int(input())
k = int(input())
if a%k==0 and b%k==0:
    print('Both')
elif a%k==0 and b%k!=0:
    print('Memo')
elif a%k!=0 and b%k==0:
    print('Momo')
else:
    print('No One')