def add(x, y):
	return x + y

def subtract(x, y):
	return x - y

def multiply(x, y):
	return x * y

def divide(x, y):
	return x / y

def power(x, y):
	return x ** y

def int_divide(x, y):
	return x // y

def mod(x, y):
	return x % y


while True:
	num1 = float(input("Enter first number: "))
	operator = input("what operation do you want to conduct: ")
	num2 = float(input("Enter second number: "))

	if operator == '+':
		print(num1, "+", num2, "=", add(num1, num2))
		break
	elif operator == '-':
		print(num1, "-", num2, "=", subtract(num1, num2))
		break
	elif operator == '**':
		print(num1, "**", num2, "=", power(num1, num2))
		break
	elif operator == '*':
		print(num1, "*", num2, "=", multiply(num1, num2))
		break
	elif operator == '//':
		print(num1, "//", num2, "=", int_divide(num1, num2))
		break
	elif operator == '/':
		print(num1, "/", num2, "=", divide(num1, num2))
		break
	elif operator == '%':
		print(num1, "%", num2, "=", mod(num1, num2))
		break
	else:
		print("""
		############################
		# Invalid Input, Try again #
		############################
		""")
