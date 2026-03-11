from numpy import*

m=array(eval(input("Digite as notas: ")))

mf=((m[0]*3.0)+(m[1]*2.0)+(m[2]*2.0)+(m[3]*3.0)/10

print(round(mf,2))

if(mf>=5.0):
	print(("aprovado").upper())
else:
	print(("reprovado").upper())