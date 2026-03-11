from numpy import*

v = array(eval(input("")))

m = ((v[0]*3) + (v[1]*2) +(v[2]*2) + (v[3]*3))/10

print(round(m,2))

if (m>=5):
	print("APROVADO")
else:
	print("REPROVADO")