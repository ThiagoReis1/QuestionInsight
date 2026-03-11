from numpy import*

v = array(eval(input()))

m = (3*v[0] + 2*v[1] + 2*v[2] + 3*v[3]) / 10 

print(round(m,2))

if(m >= 5):
	print("APROVADO")
else: 
	print("REPROVADO")