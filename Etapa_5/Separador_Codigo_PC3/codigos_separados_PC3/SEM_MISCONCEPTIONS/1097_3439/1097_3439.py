valor = int(input("qual o numero: "))
n1 = valor // 1000
n2 = valor % 1000
calculo = (n1-n2)**2
if(valor == calculo):
	msg = "atende"
	print(msg)
else:
	msg = "nao atende"
	print(msg)
print(valor)
	
