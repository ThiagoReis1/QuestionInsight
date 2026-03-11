escolha = input("Escolha T para torta ou P para pastel: ").upper()
quantia = int(input("A Quantidade de Fatias de Torta ou Pasteis: "))
capuc = int(input("Escreva a Quantidade de Capuccinos: "))

if escolha == "T":
	total = quantia * 6 + capuc * 4.50
else:
	total = quantia * 5 + capuc * 4.50

float(total)
print(round(total, 2))