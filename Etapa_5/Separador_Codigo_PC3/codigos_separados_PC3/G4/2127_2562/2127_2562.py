from numpy import*

m=array(eval(input("notas: ")))
mf=(sum(m)-min(m))/3

if(mf>=50.0):
	print(round(mf, 2))
	print("APROVADO")
else:
	print(round(mf, 2))
	print("REPROVADO")