escolha = input("B ou F: ")
quant = int(input("quant: "))
quantc = int(input("cafe: "))

bolo = quant * 3
crois = quant * 6
cafe = quantc * 5.50

if escolha == "B":
	total = bolo + cafe
else:
	total = crois + cafe
print(total)