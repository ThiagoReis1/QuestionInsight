o=15.9994
c=12.011
n=14.00674
h=1.00794
a=input("aminoacido: ").upper()

if(a!="ALANINA" and a!="VALINA" and a!="TIROSINA"):
	print("Entrada: ", a)
	print("Dado Invalido")
else:
	if(a == "ALANINA"):
		soma=((c*3)+(h*7)+(n*1)+(o*2))
		print(round(soma,2))
	if(a == "VALINA"):
		soma1=((c*5)+(h*11)+(n*1)+(o*2))
		print(round(soma1,2))
	if(a == "TIROSINA"):
		soma2=((c*9)+(h*11)+(n*1)+(o*3))
		print(round(soma2,2))		