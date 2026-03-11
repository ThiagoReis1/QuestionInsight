from numpy import*
x = array(eval(input("")))
m = (x[0]*5.0 + x[1]*3.0 + x[2]*2.0)/10.0

if m>=5:
	print(round(m,2))
	print("APROVADO")
else:
	print(round(m,2))
	print("REPROVADO")