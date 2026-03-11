precoant = float(input("Qual o preco antigo? "))

if (precoant <= 100):
	novovalor = ((precoant * (0.05)) + precoant)
	mensg = ("Aumento de 5 porcento")
	
else:
	novovalor = ((precoant * (0.15)) + precoant)
	mensg = ("Aumento de 15 porcento")
	
print(round(novovalor, 2),("ryous"))
print(mensg)