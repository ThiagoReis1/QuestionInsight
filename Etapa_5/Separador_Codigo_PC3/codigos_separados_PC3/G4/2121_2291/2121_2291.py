from numpy import*
v = array(eval(input("")))

mf = (v[0] * 5) + (v[1] * 3) + (v[2] * 2)
nota = mf / 10


print(round(nota,2))

if nota >= 5:
	print("APROVADO")
else:
	print("REPROVADO")
