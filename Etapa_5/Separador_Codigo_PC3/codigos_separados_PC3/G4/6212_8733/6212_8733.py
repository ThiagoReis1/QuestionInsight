num = int(input("Numero: "))
ter = 0

while num != -1:
	if 81 >= num >= 26:
		ter = ter + 1
	num = int(input("Numero: "))
	
print(ter)