valor = int(input("Digite o valor: "))

n = 0

while(valor >= 0):
	if(valor >= 0 and valor <= 25):
		n = n + 1
	valor = int(input("Digite o valor: "))
print(n)