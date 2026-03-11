x = float(input("Qual o valor de x? "))
if ( x <= -1) or ( x >= 1):
	eq = abs(x ** (1/2))
elif ( -1 < x < 0) or (0 < x < 1):
	eq = abs(x)
else:
	eq = 0
print(round(eq,2))