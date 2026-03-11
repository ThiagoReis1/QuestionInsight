num = int(input("Informe a idade: "))
cont = 0

while(num != -1):
	if(num < 18 and num >= 0):
		cont += 1
	num = int(input("Digite um numero: "))

print(cont)