from numpy import*

nota = array(eval(input()))

med = (nota[0]*5 + nota[1]*2.5 + nota[2]*2.5)/10
print(round(med,2))

if med >=5:
	print("APROVADO")
else:
	print("REPROVADO")

