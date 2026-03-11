from numpy import*
v = array(eval(input()))

nota = round((v[0]*5 + v[1]*2.5+v[2]*2.5)/10,2)

print(nota)

if nota>= 5:
	print("APROVADO")
else:
	print("REPROVADO")