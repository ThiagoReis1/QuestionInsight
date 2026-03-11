from numpy import*

notas = array(eval(input("digite as notas: ")))
mf=(sum(notas)-min(notas))/3

if(mf >= 50.0):
	print(round(mf,2))
	print("APROVADO")
else:
	print(round(mf,2))
	print("REPROVADO")