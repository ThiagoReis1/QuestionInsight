x=float(input("digite nota um:"))
y=float(input("digite nota dois:"))
z=float(input("digite nota tres"))
a=float(input("digite nota quatro"))
n=(x+y+z+a)/4
if (n>=7):
	print(round(n, 2))
	print("Aprovado")
else: 
	print(round(n, 2))
	print("Reprovado")