from numpy import*

notas = array(eval(input("notas: ")))

mf = (sum(notas)-min(notas))/3.0

print(round(mf,2))

if(mf>50.0):
	print("APROVADO")
else:
	print("REPROVADO")