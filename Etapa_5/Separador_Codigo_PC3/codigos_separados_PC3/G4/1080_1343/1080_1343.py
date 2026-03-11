x=float(input("Insira a primeira nota:"))
y=float(input("Insira a segunda:"))
z=float(input("Insira a terceira:"))

a=(x+y+z)/3

if (a>=5):
	print(round(a,1))
	print("Aprovado")
else:
	print(round(a,1))
	print("Reprovado")
