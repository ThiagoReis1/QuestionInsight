n1 = float(input("Escreva a nota 1: "))
n2 = float(input("Escreva a nota 2: "))
n3 = float(input("Escreva a nota 3: "))
n4 = float(input("Escreva a nota 4: "))
ma = (n1+n2+n3+n4)/4

if(ma >= 5):
	print((round(ma,2)),"Aprovacao")
else:
	print((round(ma,2)),"Reprovacao")