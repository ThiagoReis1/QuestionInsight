#Cinco provas
#Prinmeira prova (p1)
p1 = float(input("nota 1:"))
#Segunda prova (p2)
p2 = float(input("nota 2:"))
#terceira prova (p3)
p3 = float(input("nota 3:"))
#quarta prova (p4)
p4 = float(input("nota 4:"))
#quinta prova (p5)
p5 = float(input("nota 5:"))


#media das provas (mp)
mp = ((p1 + p2 + p3 + p4 + p5)/5)

if(mp>=7.0):
	print(round(mp,2))
	print("Aprovacao")
else:
	print(round(mp,2))
	print("Reprovacao por nota")