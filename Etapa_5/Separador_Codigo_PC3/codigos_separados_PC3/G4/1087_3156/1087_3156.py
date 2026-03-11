n1=float(input())
n2=float(input())
n3=float(input())
n4=float(input())

m=(n1+n2+n3+n4)/(4)
x=round(m, 2)

if(x>=7):
	print(x)
	print("Aprovado")
else:
	print(x)
	print("Reprovado")