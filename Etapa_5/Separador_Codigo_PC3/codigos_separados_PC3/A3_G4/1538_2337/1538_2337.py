x = float(input("Digite X: "))
k = float(input("Digite K: "))

cont = 0
y = 0
n = 0
while cont > k:
	y = y + (-1)**n 
	cont = cont + 2
	n = n+1
print(round(cont,9))

