from numpy import*
nota = array(eval(input(": ")))
mf = (nota[0]*3.0+nota[1]*3.0+nota[2]*4.0)/10 
print(round(mf,2))
if(mf>=5):
	print("APROVADO")
else:
	print("REPROVADO")