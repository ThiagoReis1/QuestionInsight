idade = float(input("digite a idade do espectador"))
if idade <12:
	preco = 20 + 1.25
elif idade == 12 :
	preco = 20 + 2.25	
elif idade >12 :
	preco = 20 + 3.25

valor = preco
	
print(round(valor, 2))
	
	