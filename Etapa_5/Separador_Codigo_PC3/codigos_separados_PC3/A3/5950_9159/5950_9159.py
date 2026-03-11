fatia = int(input("se for fatia de torta (T), se for pastel (P): ")).upper()
qtd_torta_pastel = int(input("Quantidade de Pastel ou torta: "))
cappucino = int(input("quantidade de cappucino: "))

if ("P"):
	total = P * 5 + cappucino
	print(round(total, 2))
else:
	total = T * 6 + cappucino
	print(round(total, 2))
	