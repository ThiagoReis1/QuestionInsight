qtd=int(input("quantidade de bilhetes:"))
tipo=input("tipo:(rede, suite, camarote)-")

r=500.00
c=1200.00
s=1500.00

vt=qtd*tipo

if tipo.lower()=="rede":
	print(round(qtd*r, 2))
elif tipo.lower()=="camarote":
	print(round(qtd*c, 2))
elif tipo.lower()=="suite":
	print(round(qtd*s, 2))
else:
	print("acomodacao invalida")