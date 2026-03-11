from numpy import*
x=array(eval(input(":")))
Mfinal=(x[0]*3.0+x[1]*2.0+x[2]*2.0+x[3]*3.0)/10.0

if(Mfinal>=5.0):
	print(round(Mfinal,2))
	print("APROVADO")
else:
	print(round(Mfinal,2))
	print("REPROVADO")