p1=float(input("Insira a nota da p1: "))
p2=float(input("Insira a nota da p2: "))
p3=float(input("Insira a nota da p3: "))
p4=float(input("insira a nota da p4: "))

soma=p1+p2+p3+p4
media=soma/4
if (media>=6):
	print(round(media,1),"Aprovado")
else:
	print(round(media,1),"Reprovado")