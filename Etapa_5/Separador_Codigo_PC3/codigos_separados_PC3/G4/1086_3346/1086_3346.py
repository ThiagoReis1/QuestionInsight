n1=float(input("nota 1:"))
n2=float(input("nota 2:"))
n3=float(input("nota 3:"))
m=round(((n1+n2+n3)/3),1)
print(round(m,1))
if(m>=7.0):
	print("Aprovado")
else:
	print("Reprovado")