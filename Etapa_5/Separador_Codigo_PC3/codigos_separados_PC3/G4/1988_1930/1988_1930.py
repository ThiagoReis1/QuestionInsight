nome=input().upper()

o= 15.9994
c=12.011
n=14.00674
h=1.00794

if(nome=="ARGININA"):
	p= (c*6)+(h*15)+(n*4)+(o*2)
	print(round(p,2))
elif(nome=="TIROSINA"):
	p1=(c*9)+(h*11)+(n)+(o*3)
	print(round(p1,2))
elif(nome=="TRIPTOFANO"):
	p2=(c*11)+(h*11)+(n*2)+(o*2)
	print(round(p2,2))
else:
	print("Entrada: ",nome)
	print("Dado Invalido")