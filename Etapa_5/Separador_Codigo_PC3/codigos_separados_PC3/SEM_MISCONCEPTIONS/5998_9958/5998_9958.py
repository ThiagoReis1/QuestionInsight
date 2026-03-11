n_macas = int(input("qual o numero de macas?" ))
if n_macas < 12:
	preco = 0.3*n_macas
else:
	preco = 0.25*n_macas
preco =(round(preco,2))
print(preco)