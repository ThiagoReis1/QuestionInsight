n1 = float(input(" Qual o valor da sua 1 nota ? : "))
n2 = float(input(" Qual o valor da sua 2 nota ? : "))
n3 = float(input(" Qual o valor da sua 3 nota ? : "))
n4 = float(input(" Qual o valor da sua 4 nota ? : "))
n5 = float(input(" Qual o valor da sua 5 nota ? : "))

ma = (n1 + n2 + n3 + n4 + n5) / 5
print(round(ma, 1))

if	(ma >= 5.0):
	msg = "Aprovado"
	
else:
	msg = "Reprovado"
	
print(msg)
	