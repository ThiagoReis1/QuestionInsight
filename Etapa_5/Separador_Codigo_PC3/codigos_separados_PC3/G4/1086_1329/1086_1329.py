x=float(input("digite nota um:"))
y=float(input("Digite nota dois:"))
z=float(input("Digite nota três:"))
a=(x+y+z)/3
if(a>=7):
	print(round(a, 1))
	print("Aprovado")
else:
	print(round(a,1))	
	print("Reprovado")	