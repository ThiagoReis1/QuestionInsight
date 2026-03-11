from numpy import*

valor = array(eval(input("Valor da compra: ")))
desconto = (sum(valor)) - (sum(valor)*0.05)
i = 0

if(len(valor)>80):
	print(round(desconto, 2))
	