a=input()
o=15.9994
c=12.011
n=14.00674
h=1.00794
ar=(c*6)+(h*15)+(n*4)+(o*2)
ti=(c*9)+(h*11)+(n)+(o*3)
tri=(c*11)+(h*11)+(n*2)+(o*2)
if((a.upper()=="ARGININA")or(a.upper()=="TIROSINA")or(a.upper()=="TRIPTOFANO")):
	if(a.upper()=="ARGININA"):
		print(round(ar,2))
	
	if(a.upper()=="TIROSINA"):
		print(round(ti,2))
	
	if(a.upper()=="TRIPTOFANO"):
		print(round(tri,2))
	
else:
	print("Entrada: ",a)
	print("Dado Invalido")
	
