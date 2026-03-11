nome=input("nome do aminoacido")
d=nome.upper()
o = 15.9994
c= 12.011
n=14.00674
h=1.00794


if (d=="ALANINA"):
	forma=(c)*3+(h)*7+(n)+(o)*2
	print(round(forma,2))
else:
	forma=(c)*5+(h)*11+(n)+(o)*2
	print(round(forma,2))
