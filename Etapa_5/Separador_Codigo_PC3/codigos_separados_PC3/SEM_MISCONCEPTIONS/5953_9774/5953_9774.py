L = 6
P = 13.5
refri = 3

com = input("[L]anche ou [P]rato executivo: ")
quantcom = int(input("Insira a quantidade de comida: "))
quantrefri = int(input("Quantidade de refrigerantes: "))

refrival = quantrefri * refri
if com == "L":
	val = L * quantcom + refrival
else:
	val = P * quantcom + refrival
	
print(round(val,2))
