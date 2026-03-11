peso = float(input("Digite o valor do pesa do saco de racao: "))

quant = float(input("Digite o valor da quantidade diarias de racao: "))

formula = peso - (quant * 5) 
	
print(round(formula, 3))
