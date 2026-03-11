L = int(input("Insira o lado aqui: "))
cont = 0
while L != -1: 
	if L == 6:
		cont += 1
	else:
		cont = cont
	L = int(input())
print(cont)