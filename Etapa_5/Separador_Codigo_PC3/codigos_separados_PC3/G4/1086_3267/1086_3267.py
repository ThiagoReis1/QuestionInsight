n1=float(input("nota1: "))
n2=float(input("nota2: "))
n3=float(input("nota3: "))
m=(n1+n2+n3)/3
print(round(m,1))
if(m >= 7.0):
	print("Aprovado")
else:
	print("Reprovado")