from numpy import*
v = array(eval(input("numeros:")))
m = (v[0] + v[1] + v[2]+v[3] - max(v))/3.0
print(round(m, 2))
if(m >= 50.0):
	msg = "APROVADO"
else:
	msg ="REPROVADO"
print(msg)