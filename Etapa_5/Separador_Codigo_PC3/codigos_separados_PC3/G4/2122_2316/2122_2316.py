from numpy import*

nota =  array(eval(input()))

med = (nota[0]*2 + nota[1] * 3 + nota[2]*5)/10
print(round(med,2))

if med >=5:
	print("APROVADO")
else:
	print("REPROVADO")
