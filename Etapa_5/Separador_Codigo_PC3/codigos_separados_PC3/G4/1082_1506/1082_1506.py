n1=float(input("nota1:"))
n2=float(input("nota2:"))
n3=float(input("nota3:"))
n4=float(input("nota4:"))
n5=float(input("nota5:"))

media= ((n1+n2+n3+n4+n5)/5)
print(round(media,1))
if(media>=5):
	print("Aprovado")
else:
	print("Reprovado")	
