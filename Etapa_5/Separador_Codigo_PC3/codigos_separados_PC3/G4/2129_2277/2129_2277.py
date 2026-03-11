from numpy import*
nota = array(eval(input(" ")))
mf = ((nota[0]*1.0)+(nota[1]*2.0)+(nota[2]*3.0)+(nota[3]*4.0))/(10.0)
print(round(mf,2))
if(mf>=5):
	print("APROVADO")
else:
	print("REPROVADO")