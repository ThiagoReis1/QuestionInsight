from numpy import *

v = array(eval(input("vetor: ")))

#v = arange(v)
mf = (sum(v) - min(v)) / 3

if( mf >= 50.0):
	print(round(mf, 2))
	print("APROVADO")
else:
	print(round(mf, 2))
	print("REPROVADO")