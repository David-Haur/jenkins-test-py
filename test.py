print("Hello World")

def show_Fibo(n):
	if n == 1 or n == 2:
		return 1
	a, b = 1, 1
	for i in range(n-2):
		c = a+b
		a, b = b, c
	return b