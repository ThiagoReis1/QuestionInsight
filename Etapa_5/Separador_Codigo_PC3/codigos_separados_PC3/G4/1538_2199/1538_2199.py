x = float(input("Valor de x:"))
k = int(input("Valor de k"))

cont = 0

ap = 1

while(cont < k):
	cont = cont + (cont + 1)
	ap = ap + (-1) ** (cont + 1) + x ** cont
	
print(ap)
	
