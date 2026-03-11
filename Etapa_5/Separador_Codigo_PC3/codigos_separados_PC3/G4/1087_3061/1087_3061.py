n1=float(input("Coloque a primeira nota aqui :"))
n2=float(input("Coloque a segunda  nota aqui :"))
n3=float(input("Coloque a terceira nota aqui :"))
n4=float(input("Coloque a quarta nota aqui :"))
ma=round((n1+n2+n3+n4)/4,2)
if(ma>=7.0):
	print(ma)
	print("Aprovado")
else:
	print(ma)
	print("Reprovado")