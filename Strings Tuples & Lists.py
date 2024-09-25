test_string = 'this is a test'
test_list = [1,2,3,4]


# print(test_string.split('t'))
# print(list(test_string))
# print(tuple(test_string))

# #turn a list/tuple into a string

# print('GAP'.join(['one','two','three','four']))
# print(type(str(test_list)))


# #indexing on strings

# print(test_string[0:5])

#exercise
#removee all the suff to only get 1 2 3 4
exercise = str(test_list).strip('[').strip(']').replace(',','').replace(' ','')
print(exercise)

