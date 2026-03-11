uni_acad = input("Qual a sua unidade academica? ").upper()

cont = 0

while (uni_acad != 'X'):
	if (uni_acad == 'FT'):
		cont = cont + 1
	uni_acad = input("Qual a sua unidade academica? ").upper()
print(cont)