aboboras = int(input("digite o numero de aboboras compradas:"))

if aboboras < 5:
	preco = aboboras * 3.80
else:
	preco = aboboras * 3.45

print(round(preco,2)) 