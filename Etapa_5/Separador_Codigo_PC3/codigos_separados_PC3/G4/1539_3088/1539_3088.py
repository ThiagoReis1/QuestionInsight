x = float(input("Insira o valor de x:"))
k = int(input("Insira o valor de k:"))
t = 0
eq = 0
while t<k:
	eq = ((-x)**t) + eq
	t = t + 1
print (round(eq,7))