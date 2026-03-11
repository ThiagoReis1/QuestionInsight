from numpy import*
v1 = eval(input())
MFinal = (v1[0] * 1.0 + v1[1] * 2.0 + v1[2] * 3.0 + v1[3] * 4.0) / 10.0
print(round(MFinal,2))
if(MFinal>=5.0):
	print("APROVADO")
else:
	print("REPROVADO")