aminoacido=input("digite o nome do aminoacido:")

o=15.9994
c=12.011
n=14.00674
h=1.00794

peso1=(c*3)+(h*7)+(n)+(o*2)
peso2=(c*5)+(h*11)+(n)+(o*2)

if(aminoacido.upper()=="ALANINA"):
	print(round(peso1,2))

else:
	print(round(peso2,2))