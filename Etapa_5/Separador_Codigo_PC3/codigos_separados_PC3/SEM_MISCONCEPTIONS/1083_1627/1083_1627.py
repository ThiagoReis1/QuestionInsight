prova1 = float(input("Qual a sua primeira nota? "))
prova2 = float(input("Qual a nota da segunda prova? "))
prova3 = float(input("Qual a nota da terceira prova? "))
m = ((prova1 + prova2 + prova3 ) / 3)
print(round(m , 2))

if(m >= 6) :
		print("Aprovado")
else:
	print("Reprovado")