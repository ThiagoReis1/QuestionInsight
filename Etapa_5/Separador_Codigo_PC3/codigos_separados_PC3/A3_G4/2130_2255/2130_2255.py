from numpy import *
nota = array(eval(input("Notas: ")))
i = 0 
mf = (nota[0] * 3.0 + nota[1] * 2.0 + nota[2] * 2.0 + nota[3] * 3.0) / 10.0
print(round(mf, 2))
if(mf >= 5.0):
	print("APROVADO")
else:
	print("REPROVADO")