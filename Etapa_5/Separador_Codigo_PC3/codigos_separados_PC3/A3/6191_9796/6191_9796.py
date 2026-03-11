moeda = input("resultado:")
cont = 0
if moeda == 'CARA':
	cont =1
while moeda != 'S':
	moeda = input("resultado:")
	if moeda == 'CARA':
		cont = cont + 1
print(cont)