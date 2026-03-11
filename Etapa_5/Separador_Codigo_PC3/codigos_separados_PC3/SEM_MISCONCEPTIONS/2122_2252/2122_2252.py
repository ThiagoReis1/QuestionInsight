from numpy import*
v = array(eval(input("quais as notas:")))
nota_final = ((v[0] * 2.0) + (v[1] * 3.0 )+ (v[2] * 5.0))/10.0
print(round(nota_final,2))
if(nota_final >= 5.0):
	print("APROVADO")
else:
	print("REPROVADO")
			