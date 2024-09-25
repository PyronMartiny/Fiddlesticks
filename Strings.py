
# # quotes for strings
# test_var = 'Test 1'
# test_var2 = "Test 2"
# print(test_var)
# print(test_var2)

# quotes for inside of strings
# test_var3 = "He said 'this was great'"
# print (test_var3)
# test_var4 ='\"\'' # simple escape character
# print(test_var4)

# # escape characters
# test_var5 = 'line 1: Some Text \nLine 2: Some More Text'
# print(test_var5)

# #multiple lines
# test_var6 = '''A comment
# Write some more text
# another one
# and another one'''
# print(test_var6)


#math and strings
# test_var7 = 'hello' + ' ' + 'world'
# test_var8 = 'copy ' * 8 
# print(test_var8)
name = 'Bob'
age = 75
# greeting_string = 'Hello {one}, you are {two} years old'.format(one = name, two =  age)
greeting_string_better = f'Hello {name}, you are {age} years old'
print(greeting_string_better)