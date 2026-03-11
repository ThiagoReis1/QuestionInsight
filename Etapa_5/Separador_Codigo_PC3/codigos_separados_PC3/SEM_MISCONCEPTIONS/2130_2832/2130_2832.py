import numpy
xs=numpy.array(eval(input()))
MFinal = ((xs[0]*3.0)+(xs[1]*2.0)+ (xs[2]*2.0)+(xs[3]*3.0))/ 10.0
MFinal=round(MFinal,2)
print(MFinal)
if MFinal>=5:
	print("APROVADO")
else:
	print("REPROVADO")
