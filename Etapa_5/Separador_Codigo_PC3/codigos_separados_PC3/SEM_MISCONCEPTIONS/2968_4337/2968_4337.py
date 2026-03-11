tipo = input("Lanche ou Salgado? ")
quantt = int(input("Digite a quantidade: "))
refri = int(input("Digite a quantidade de refrigentes: "))
total1 = float(3.5 * quantt + 4 * refri)
total2 = float(5 * quantt + 4 * refri)
if(tipo.upper() == "S"):
	print(round(total1,2))
if(tipo.upper() == "L"):
	print(round(total2,2))
#n = float(input())
#print(round(n,2))