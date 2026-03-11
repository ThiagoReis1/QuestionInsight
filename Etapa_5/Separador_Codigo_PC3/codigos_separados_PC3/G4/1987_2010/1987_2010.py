ami=(input("informe o aminoacido: ")).upper()

o=15.9994
c=12.011
n= 14.00674
h=1.00794

if(ami == "ALANINA"):
	p= (c*3) + (h*7) + n + (o*2)
	print(round(p,2))
elif(ami == "VALINA"):
	pe= (c*5) + (h*11) + n + (o*2)
	print(round(pe,2))
elif(ami == "TIROSINA"):
	pes= (c*9) + (h*11) + n + (o*3)
	print(round(pes,2))
else:
	print("Entrada:", ami)
	print("Dado Invalido")
	