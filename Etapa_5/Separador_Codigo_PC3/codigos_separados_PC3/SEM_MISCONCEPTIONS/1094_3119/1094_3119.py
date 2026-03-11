numero = int(input("digite o numero:"))
n01 = numero // 100
resto_n01 = numero % 1
n02 = resto_n01
valor = (n01 + n02 ) ** 2
if  (valor == numero):
    texto = "atende"
else:
	 texto = "nao atende"
		
print(texto)
print(numero)

