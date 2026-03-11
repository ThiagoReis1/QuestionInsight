from numpy import*

custo = array(eval(input("")))
#custo = ([26.5,134.3,1.1])
cont = 0
valor_final = 0
desconto = 0

while(cont < size(custo)):
	if(custo[cont] > 80.0):
		desconto += custo[cont] * 15 / 100

	cont +=1

valor_final = sum(custo)- desconto
print(round(valor_final, 2))