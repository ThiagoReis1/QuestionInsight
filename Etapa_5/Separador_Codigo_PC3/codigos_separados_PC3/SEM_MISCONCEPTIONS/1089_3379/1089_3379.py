valor1= float(input("Insira o valor da compra 1 "))
valor2= float(input("Insira o valor da compra 2 "))
valor3= float(input("Insira o valor da compra 3 "))
limite= float(input("Insira o limite do cartao "))
total= round(valor1+valor2+valor3,2)
if total<=limite:
	print(total,"Nao ultrapassou")
else:
	print(total,"Ultrapassou")