a = input("Insira C para coxinha e E para esfirra:")


if a.upper() == "C":
	c = int(input("quantidade de coxinhas:"))
	sucos = int(input("Quantidade de sucos:"))
	total = c*2 + sucos*6
else:
	e = int(input("quantidade de esfirras:"))
	sucos = int(input("Quantidade de sucos:"))
	total = e*4.5 + sucos*6
print(total)