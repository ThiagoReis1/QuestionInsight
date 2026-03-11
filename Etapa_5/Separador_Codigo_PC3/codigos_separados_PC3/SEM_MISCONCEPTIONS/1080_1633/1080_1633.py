prova1 = float(input("Qual a sua primeira nota ?"))
prova2 = float(input("Qual a sua segunda nota?"))
prova3 = float(input("Qual a sua terceira nota?"))
m = ((prova1 + prova2 + prova3) / 3)
print(round(m , 1))

if(m >= 5) :
	print("Aprovado")
else:
	print("Reprovado")