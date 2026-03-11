ano_nascimento = int(input("Ano de nascimento: "))
pais = input("B ou R :").upper()

x = 2023 - ano_nascimento

ibn = 18 - x
ibs = x - 18
irn = 21 - x
irs = x - 21

if pais == "B" and x >= 18:
	print("sim")
	print(ibs)
elif pais == "B" and x <= 18:
	print("nao")
	print(ibn)
elif pais == "R" and x >= 21:
	print("sim")
	print(irs)
elif pais == "R" and x <= 21:
	print("nao")
	print(irn)
elif (pais != "B" or pais != "R"):
	print("invalido")
