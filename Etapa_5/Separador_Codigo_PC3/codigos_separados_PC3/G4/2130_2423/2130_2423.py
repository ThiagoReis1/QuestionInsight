from numpy import*
nota = array(eval(input("Notas parciais: ")))

mf = (nota[0] * 3 + nota[1] * 2 + nota[2] * 2 + nota[3] * 3) / 10

if(mf >= 5):
	msg = "APROVADO"
else:
	msg = "REPROVADO"
	
print(round(mf,2))
print(msg)