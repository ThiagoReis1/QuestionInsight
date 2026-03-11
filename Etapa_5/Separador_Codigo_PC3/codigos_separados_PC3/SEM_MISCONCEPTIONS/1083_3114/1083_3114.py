prova1 = float(input("nota: "))
prova2 = float(input("nota: "))
prova3 = float(input("nota: "))

med = (prova1 + prova2 + prova3) / 3

if (med >= 6):
	mens = ("Aprovacao")
	
else:
	mens = ("Reprovacao")
	
print(round(med, 2))
print(mens)