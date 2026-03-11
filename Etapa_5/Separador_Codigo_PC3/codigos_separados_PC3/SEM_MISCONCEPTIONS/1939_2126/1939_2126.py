nome_amin = input("Nome do amino: (ASPARAGINA/TRIPTOFANO)")
nome1 = "ASPARAGINA"
nome2 = "TRIPTOFANO"
o = 15.999
c = 12.011
n = 14.00674
h = 1.00794
if(nome_amin.upper()==nome1):
	a = (c*4)+(h*8)+(n*2)+(o*3)
	print (round(a,2))

if(nome_amin.upper()==nome2):
	b = (c*11)+(h*11)+(n*2)+(o*2)
	print (round(b,2))
