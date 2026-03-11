x = int(input("Insira o Valor de X (sempre impar): "))
y = int(input("Insira o Valor de Y: "))

cont = x
acu = 0

while cont <= y:
	if cont % 2 == 0:
		cont += 1
	else:
		acu += cont
		cont += 1
		
print(acu)