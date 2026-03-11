#Entradinhas
p1 = float(input("Insira a primeira nota: "))
p2 = float(input("Insira a segunda nota: "))
p3 = float(input("Insira a terceira nota: "))
p4 = float(input("Insira a quarta nota: "))
p5 = float(input("Insira a quinta nota: "))
#Calculando média
m = (p1+p2+p3+p4+p5)/5
#Condições
if(m >= 6 ):
	print(round(m,2))
	print("Aprovacao")
else:
	print(round(m,2))
	print("Reprovacao")

