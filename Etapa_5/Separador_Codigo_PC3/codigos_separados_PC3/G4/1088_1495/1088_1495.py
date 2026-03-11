# Rodrigo de Oliveira Brasil Ferreira - 21602328
# Prova 02
# 07 / 07 / 2016
# Engenharia Quimica

n1 = float(input("digite a nota 1: "))
n2 = float(input("digite a nota 2: "))
n3 = float(input("digite a nota 3: "))
n4 = float(input("digite a nota 4: "))
n5 = float(input("digite a nota 5: "))
x = (n1 + n2 + n3 + n4 + n5) / 5
print(round(x, 2))
if(x >= 7):
	print("Aprovacao")
else:
	print("Reprovacao")	
	