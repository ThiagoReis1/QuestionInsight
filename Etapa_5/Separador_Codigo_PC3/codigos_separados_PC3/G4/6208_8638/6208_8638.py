num = int(input("numero da sorte: "))
cont = 0
while num != -1:
	if 51 <= num <= 75:
		cont = cont + 1
	num = int(input("numero da sorte: "))
print(cont)