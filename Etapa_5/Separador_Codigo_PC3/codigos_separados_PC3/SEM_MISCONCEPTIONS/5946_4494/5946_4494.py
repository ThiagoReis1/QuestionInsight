item = input("Digite a letra do item:\n")
qttdI = int(input("Digite a quantidade do item:\n"))
qttdR = int(input("Digite a quantidade de refrigerantes:\n"))

if item.upper() == "L":
	total = qttdI * 6 + qttdR * 3
else:
	total = qttdI * 4.5 + qttdR * 3

print(round(total, 1))