from numpy import*
v = array(eval(input(":")))
mf = (v[0]*3 + v[1]*3 + v[2]*4)/10

print(round(mf,2))
if(mf >=5):
	print("APROVADO")
else:
	print("REPROVADO")