prova1 = float(input("nota1: "))
prova2 = float(input("nota2: "))
prova3 = float(input("nota3: "))
m = ((prova1 + prova2 + prova3)/3)
print(round(m, 2))

if (m >= 6.0):
	print ("Aprovacao")
else:
   print("Reprovacao")