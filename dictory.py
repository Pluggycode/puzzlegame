# my_dict = { 'feature':['aspect','angle'], 'art':['painting','sculpture'] }
# search = input('Enter a word to search: ')
# if search in my_dict:
#     print(my_dict[search])
# else:
#     print('The word is not found in the dictionary')

# tuple_name = ('audi', 'benz', 'BMW', 'audi')
# print(tuple_name)
# print(tuple_name[0])

# p = tuple_name.count('audi')
# print(p)
# i = tuple_name.index('benz')
# # print(i)

# set = {1,2,3,4,5,6,7,8,9,10}
# print(set)

A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)  # {1, 2, 3, 4, 5}
print(A & B)  # {3}
print(A - B)  # {1, 2}

print(A ^ B)
