# Monalisa Pereira 21600560
# 300616
# Av 02 - Ex 01

p1 = float(input("Insira da nota da P1: "))
p2 = float(input("Insira a nota da P2: "))
p3 = float(input("Insira a anota da P3: "))

media = (p1 + p2 + p3) / 3

if (media >= 5.0):
	resultado = "Aprovado"
else:
	resultado = "Reprovado"
	
print(round(media, 1))
print(resultado)