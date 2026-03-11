# Entradas
res = input("Resultado do time na competição: ").lower()
vez = input("Quantas vezes o time chegou ao resultado: ").lower()

# Condições
if ((res == "campeao") and (vez == "06-vezes")):
	print(("Corinthians").upper())
elif ((res == "campeao") and (vez == "03-vezes")):
	print(("Santos").upper())
elif ((res == "vice-campeao") and (vez == "01-vez")):
	print(("Flamengo").upper())
elif ((res == "vice-campeao") and (vez == "06-vezes")):
	print(("Internacional").upper())
else:
	print(("TIME DE FUTEBOL NAO IDENTIFICADO").upper())
