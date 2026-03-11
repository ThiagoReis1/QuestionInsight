from numpy import *
v = array(eval(input("v: ")))
nota_final = (v[0]*3 + v[1]*3 + v[2]*4)/10
if (nota_final >= 5):
	print(round(nota_final,2))
	print("APROVADO")
else:
	print(round(nota_final,2))
	print("REPROVADO")