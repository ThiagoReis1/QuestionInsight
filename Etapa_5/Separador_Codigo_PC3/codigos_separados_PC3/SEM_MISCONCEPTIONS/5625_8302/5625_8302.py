escolha = input("tapioca ou salgado: ")
qtd = int(input("qtd de tapiocas ou salgado: "))
acai = int(input("qtd de acais: "))

S = (4.00 * qtd) + (acai * 10.00)
T = (5.50 * qtd) + (acai * 10.00)

if escolha == "S": 
	result = S
else:
	result = T
	
print(result)