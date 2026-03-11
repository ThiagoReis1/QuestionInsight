from numpy import *

media = array(eval(input()))

n0 =media [0]
n1 = media [1]
n2 = media [2]
n3 = media [3]
nf =(n0*3.0 + n1*2.0 + n2*2.0 + n3*3.0) /10.0

print(round(nf,2))

if(nf >= 5):
	print("APROVADO")
else:
	print("REPROVADO")