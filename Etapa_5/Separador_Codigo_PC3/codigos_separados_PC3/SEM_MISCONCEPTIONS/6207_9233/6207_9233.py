num = int(input("digite os numeros: "))
contadora = 0

while num != -1:
	if 26 <= num <= 50:
		contadora = contadora + 1
	num = int(input("digite a quantidade de numeros: "))
print(contadora)