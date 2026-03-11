prova1 = float(input("nota1: "))
prova2 = float(input("nota2: "))
prova3 = float(input("nota3: "))
prova4 = float(input("nota4: "))

med = (prova1 + prova2 + prova3 + prova4) / 4 
print(round(med, 2))

if (med >= 5.0):
	msg = "Aprovacao"
else:
	msg = "Reprovacao"
	
print(msg)