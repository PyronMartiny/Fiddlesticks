
def better_calculator(num1, num2, operation):
	if operation == 'plus':
		result = num1 + num2
	elif operation == "minus":
		result = num1 - num2
	print(f'{num1} {operation} {num2} = {result}')

#
better_calculator(16346346, 2346346, 'minus')
better_calculator(1,5,'plus')