face = int(input("digite um numero:"))

cont = 0
cont_6 = 0

while face != -1:
	if face == 5:
		cont = cont + 1
		cont_6 = cont_6 + 1
	else:
		cont = cont + 1
		cont_6 = cont_6
	face = int(input("digite um numero:"))
	
valor = (cont_6/cont) * 100
print(cont)
print(round(valor,2))