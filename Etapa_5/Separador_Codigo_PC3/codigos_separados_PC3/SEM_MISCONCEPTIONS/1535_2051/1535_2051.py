x= int(input("valor de x"))
i = int (input("quantidade de termos"))

cont=0
serie = 0
while (cont<i):
	cont=cont+ 1
	arctg = x**(cont+2)/cont+2
	sinal = -1

	serie= serie + arctg*sinal
	
	
	
	
print(round(serie,6))