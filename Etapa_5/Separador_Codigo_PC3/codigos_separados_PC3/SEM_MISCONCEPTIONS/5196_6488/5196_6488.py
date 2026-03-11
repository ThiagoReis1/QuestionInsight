antigo = float(input("Digite o preco para ser corrigido: "))

if(antigo <= 100):
	novo = antigo + (5/100) * antigo
	percentual = "Aumento de 5 porcento"
else:
	novo = antigo + (15/100) * antigo
	percentual = "Aumento de 15 porcento"
	
print(round(novo, 2), "ryous")
print(percentual)