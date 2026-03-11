num = int(input("Digite o numero: "))

cont = 0
six = 0
while(num != -1):
	if(num == 6):
		six = six + 1
	num = int(input("Digite outro numero: "))
	cont = cont + 1
print(cont)
print(round(100*(six / cont), 2))