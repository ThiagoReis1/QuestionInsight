from numpy import*

nota=array(eval(input()))
mf=(nota[0]*5+nota[1]*2.5+nota[2]*2.5)/10
print(round(mf, 2))

if(mf>=5):
	print("APROVADO")
else:
	print("REPROVADO")