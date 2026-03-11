numero= int(input("valor:"))
n01= numero // 100
resto_n01= numero % 1
n02= resto_n01 // 1
form= (n01-n02) ** 4
if(form == numero):
	texto=("nao atende")
else:
	texto= ("atende")
print(texto)
print(numero)
	
	