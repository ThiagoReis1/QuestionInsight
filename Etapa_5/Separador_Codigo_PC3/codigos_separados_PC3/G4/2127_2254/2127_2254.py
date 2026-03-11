from numpy import*
v = array(eval(input(":")))
m = (v[0] + v[1] + v[2] + v[3] - min(v))/(3.0)
print(round(m,2))
if(m >=50.0):
	print("APROVADO")
else:
	print("REPROVADO")