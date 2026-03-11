altC= 1.8
taxaC = 0.01

alt = float(input())
taxa = float(input())
cont = 0

while alt < altC:
	alt += taxa
	altC += taxaC
	cont += 1

print(cont)