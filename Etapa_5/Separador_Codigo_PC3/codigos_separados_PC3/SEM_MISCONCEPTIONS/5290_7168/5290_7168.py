cont = 0
cont5 = 0
jogadas = int(input("jogue o dado de dez lados:" ))

while (jogadas != -1) and (jogadas <= 10):
	if jogadas != 5:
		cont = cont + 1	
		jogadas = int(input("jogue o dado de dez lados novamente: "))
	else:
		cont5 = cont5 + 1
		cont = cont +1
		jogadas = int(input("joga: "))
print(cont)