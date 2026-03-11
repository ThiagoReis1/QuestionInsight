from numpy import*

N = array(eval(input("notas: ")))

M = sum(N) - min(N)
Mf = M /3

if(Mf>=50.0):
	print(round(Mf,2))
	print("APROVADO")
else:
	print(round(Mf,2))
	print("REPROVADO")
	