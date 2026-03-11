valor = int(input("Valor do BogoMips:"))
bg = 7206.14
cont = 2018

while (valor <= bg):
	cont = cont+1
	bg = bg + (bg*0.65)
	print (cont)