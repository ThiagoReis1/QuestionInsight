from numpy import*
v = array(eval(input()))
mf = (v[0]*5.0 + v[1]*2.5+ v[2]*2.5)/10.0
print(round(mf, 2))
if(mf >= 5.0 ):
	print("APROVADO")
else:
	print("REPROVADO")			