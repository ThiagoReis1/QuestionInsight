resposta = input().upper()
contador = 0

while resposta != "X":
	if resposta == "S":
		contador += 1
	resposta = input().upper()


print(contador)