from numpy import *
x = array(eval(input("notas: ")))

i = 0
nf = (5*x[0] + 3*x[1] + 2*x[2])/10

print(nf)
if(nf<5):
	print("REPROVADO")
else:
	print("APROVADO")
	