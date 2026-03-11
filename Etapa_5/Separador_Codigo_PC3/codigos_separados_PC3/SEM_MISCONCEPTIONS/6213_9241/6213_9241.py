numeros= int(input("digite os numeros: "))
contagem = 0

while numeros != -1:
	if 101 <= numeros <= 201:
		contagem= contagem + 1
	numeros= int(input("digite a quantidade de numeros: "))
print(contagem)