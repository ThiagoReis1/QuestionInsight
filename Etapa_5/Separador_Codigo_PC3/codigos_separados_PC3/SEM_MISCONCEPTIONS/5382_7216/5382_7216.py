from numpy import*

etiqueta = input("").upper()
i = 0
soma_preco = 0 

while i < len(etiqueta):
	if etiqueta[i] == 'A'or etiqueta[i] == 'E' or etiqueta[i] == 'O' or etiqueta[i] == 'U' or etiqueta[i] == 'I':
		soma_preco = soma_preco+0.25

	else:
		soma_preco = soma_preco+0.27
	i = i+1
print(round(soma_preco,2))
	