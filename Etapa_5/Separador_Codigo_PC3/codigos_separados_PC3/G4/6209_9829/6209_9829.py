num = 1

cont = 0

while num != -1:
	num = int(input("Escolha um numero"))
	if num >= 76 and num <= 100:
		cont += 1
	
print(cont)