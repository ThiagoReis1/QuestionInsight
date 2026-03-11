#Universidade federal do Amazonas
#Engenharia de producao
#Inroducao a Ciencia dos compuadores
#Allan Bezerra - 21552438

n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
n3 = float(input("Terceira nota: "))
n4 = float(input("Quarta nota: "))
n5 = float(input("Quinta nota: "))

m = (n1+n2+n3+n4+n5)/5

if (m >= 6):
	print(round(m,2))
	print("Aprovado")
else:
	print(round(m,2))
	print("Reprovado")
