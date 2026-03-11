nome = input("nome do amido:(GLUTAMINA ou TREONINA) ")
nome1 = "GLUTAMINA"
nome2 = "TREONINA"
o = 15.9994
c = 12.011
n = 14.0067
h = 1.00794
if(nome.upper()==nome1):
	a = (c*5) + (h*8) + (n*1) + (o*4)
	print(round(a,2))

if (nome.upper()==nome2):
	b = (c*4) + (h*9) + (n*1) + (o*3)
	print (round(b,2))


