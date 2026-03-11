a = int(input("numero a ser digitado:"))
cont = 0
cont2 = 0
while(a != 0):
	cont = cont + 1
	if(a % 2 == 0):
		cont2 = cont2 + 1
	a = int(input("numero a ser digitando:"))
cont2 = (cont2 / cont) * 100
print(cont)
print(round(cont2 , 2))