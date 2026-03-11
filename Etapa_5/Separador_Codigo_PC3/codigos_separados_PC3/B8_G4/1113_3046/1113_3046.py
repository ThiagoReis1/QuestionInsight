i = int(input("informe a idade: "))
p = float(input("informe o peso: "))

print("Entradas:", i, "anos e", p, "kg")

if((i < 0) or (i > 130) or (p < 0) or (p > 550)):
	print("Dados invalidos")
elif((0 <= i <= 20) and (0 <= p <= 60)):
	print("Grupo de risco: 9")
elif((0 <= i <= 20) and (60 <= p <= 90)):
	print("Grupo de risco: 8")
elif((0 <= i <= 20) and (p > 90)):
	print("Grupo de risco: 7")
elif((20 < i <= 50) and (0 <= p <= 60)):
	print("Grupo de risco:  6")
elif((20 < i <= 50) and (60 <= p <= 90)):
	print("Grupo de risco: 5")
elif((20 < i <= 50) and (p > 90)):
	print("Grupo de risco: 4")
elif((i > 50) and (0 <= p <= 60)):
	print("Grupo de risco: 3")
elif((i > 50) and (60 <= p <= 90)):
	print("Grupo de risco: 2")
elif((i > 50) and (p > 90)):
	print("Grupo de risco: 1")
	
	