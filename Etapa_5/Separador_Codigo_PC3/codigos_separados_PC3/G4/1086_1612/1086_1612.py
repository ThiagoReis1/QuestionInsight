n1 = float(input("nota1:"))
n2 = float(input("nota2:"))
n3 = float(input("nota3:"))

media = (n1+n2+n3)/3
print(round(media,1))

if(media>=7):
	print("Aprovado")
else:
	print("Reprovado")