from numpy import*


v = array(eval(input("Notas parciais: ")))

mf = (v[0]*1 + v[1]*2 + v[2]*3 + v[3]*4)/10

print(round(mf,2))
if(mf>=5):
	print("APROVADO")
else:
	print("REPROVADO")