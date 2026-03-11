from numpy import * 

custo = array(eval(input("digite o custo dos itens: ")),dtype=float)
desconto = 0.08
total = 0
for i in range(size(custo)):
	if(custo[i] >= 50):
		desconto = desconto - 0.08 * custo[i]
		total = total + 1
	elif(custo[i] > 50):
		total =  total + 1
		
print(round(custo,1))