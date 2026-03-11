o = 15.9994
c = 12.011
ni = 14.00674
h = 1.00794
n = input("Nome do aminoácido: ").upper()

if(n!="ARGININA" and n!="TIROSINA" and n!= "TRIPTOFANO"):
	print("Entrada:", n)
	print("Dado Invalido")
elif(n=="ARGININA"):
	ca = (c*6) + (h*15) + (ni*4) + (o*2)
	print(round(ca,2))
elif(n=="TIROSINA"):
	cb = (c*9) + (h*11) + (ni) + (o*3)
	print(round(cb,2))
else:
	cc = (c*11) + (h*11) + (ni*2) + (o*2)
	print(round(cc,2))
