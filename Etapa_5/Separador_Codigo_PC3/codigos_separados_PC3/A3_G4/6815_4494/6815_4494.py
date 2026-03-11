n = int(input())
cont = 1
raiz = 1

while cont <= n:
	raiz = cont**(0.5)
	print(round(raiz, 2))
	cont += 1
	
print("fim")