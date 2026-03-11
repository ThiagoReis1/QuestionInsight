numero = int(input(" numero fornecido: "))
dig1 = numero//10000
dig2 = (numero%10000)//100
dig3 = (numero%100)
x = (dig1**3)+(dig2**3)+(dig3**3)
if(x==numero):
	print("atende")
	print(numero)
else:
	print("nao atende")
	print(numero)