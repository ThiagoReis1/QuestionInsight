x = float(input("digite o valor de x:"))

if ( x <= -1 or x >= 1):
	conta = x ** 2
elif ( x > -1 and x < 0 or x > 0 and x < 1):
	conta = x
elif ( x == 0):
	conta = 1
print(conta)