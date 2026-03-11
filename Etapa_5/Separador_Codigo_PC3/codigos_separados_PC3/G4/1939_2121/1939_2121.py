nome=str(input("Asparagina/Triptofano:"))
o=15.999
c=12.011
n=14.00674
h=1.00794
a=c*4 +h*8 + n*2 + o*3
t=c*11 + h*11 + n*2 + o*2
if(nome.upper()=="ASPARAGINA"):
	print(round(a,2))
else:
	print(round(t,2))