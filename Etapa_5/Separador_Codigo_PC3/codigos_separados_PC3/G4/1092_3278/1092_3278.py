numero = int(input("numero fornecido: "))
print (numero)
d1 = numero // 1000
d2 = (numero // 100)%10 
d3 = (numero // 10)%10 
d4 = numero%10
if ((d2 + d4)% (d1 + d3) !=0):
	print ("atende")
else:
	print ("nao atende")