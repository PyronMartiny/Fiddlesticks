# exercise 1

# def function(num1, num2):
#     product = num1 * num2
#     add = num1 + num2
#     if product <= 1000:
#         print(product)
#     else:
#         print(add)

# function(40,30)

#exercise 2

# previous_num = 0

# for i in range(1, 11):
#     x_sum = previous_num + i
#     print("Current Number:", i,"Previous Number:", previous_num, "Sum:", x_sum)

# Exercise 3

# String = input('this is the input ')
# print('Original String:', String)

# size = len(String)

# print('only even index characters: ')

# for i in range(0, size - 1, 2):
#     print("index[", i, "]", String[i])

#exercise 4

# def remove_chars(word, n):
#     print('Original string:', word)
#     x = word[n:]
#     return x

# print("Removing characters from a string")
# print(remove_chars("pynative", 4))
# print(remove_chars("pynative", 2))

# exercise 5

# numbers_x = [10, 20, 30, 40, 10]
# numbers_y = [75, 65, 35, 75, 30]

# def first_and_last(number_list):
#     print ('This is the number list:', number_list)
#     num1 = number_list[0]
#     num2 = number_list[4]
#     if num1 == num2:
#         return True
#     else:
#         return False

# print ('Result is:', first_and_last(numbers_x))
# print ('Result is:', first_and_last(numbers_y))

# exercise 6

# give_list = [10,20,33,46,55]

# for i in give_list: 
#     if i % 5:
#         continue
#     else:
#         print (i)

#ALTERNATIVE SOLUTION:

# num_list = [10, 20, 33, 46, 55]
# print("Given list:", num_list)
# print('Divisible by 5:')
# for num in num_list:
#     if num % 5 == 0:
#         print(num)

# # exercise 7

# str_x = 'Emma is a good developer. Emma is a writer'
# print('There are', str_x.count('Emma'), 'occurences of Emma in this string')

# for x in range(1,6):
#     print(x)

for num in range(10):
    for i in range(num):
        print (num, end=" ") #print number
# new line after each row to display pattern correctly
    print("\n")