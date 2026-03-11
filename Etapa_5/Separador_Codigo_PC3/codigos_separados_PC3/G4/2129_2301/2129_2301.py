from numpy import*
v = array(eval(input()))

nota= round((v[0]*1 + v[1]*2 + v[2]*3+ v[3]*4)/10,2)

print(nota)

if nota>= 5:
	print("APROVADO")
else:
	print("REPROVADO")