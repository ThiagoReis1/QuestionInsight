num = int(input("Digite o numero"))

cont= 0

while (num != -1):
	if (num >= 26) and (num <= 85):
		cont= cont + 1 
	num = int(input("Digite o numero"))
print(cont)