from numpy import*

notas = array(eval(input("Digite as 4 notas: ")))
MF = ((notas[0]*1)+(notas[1]*2)+(notas[2]*3)+(notas[3]*4))/10
print(round(MF , 2))
if(MF>=5):
	print("APROVADO")
else:
	print("REPROVADO")
	i