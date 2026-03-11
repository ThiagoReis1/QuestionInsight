an = int(input("Ano de Nascimento: "))
p = input("Pais B para Brasil, J para Japao: ").upper()

total = 2023 - an
if p == "B" and total >=21:
	apt = total - 21
	print("sim")
	print(apt)
elif p == "B" and total<21 :
	napt = 21-total
	print("nao")
	print(napt)	
elif p == "J" and total >= 20:
	apt = total - 20
	print("sim")
	print(apt)
elif p == "J" and total<20:
	napt = 20 -  total
	print("nao")
	print(napt)
else:
	print("invalido")