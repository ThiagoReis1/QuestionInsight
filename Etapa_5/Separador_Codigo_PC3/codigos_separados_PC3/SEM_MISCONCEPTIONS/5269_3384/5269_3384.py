n = int(input("Digite o numero: "))

total = 0
multiplos = 0

while n != 0:
	if n % 3 == 0:
		multiplos = multiplos + 1
	total = total + 1
	n = int(input("Digite o numero: "))
print(total)
print(round((multiplos/total) * 100 , 2))