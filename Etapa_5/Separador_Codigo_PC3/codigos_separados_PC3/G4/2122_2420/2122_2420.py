from numpy import*
np = array(eval(input('nota do aluno: ')))
NF = (np[0]*2.0 + np[1]*3.0 + np[2]*5.0)/10
print(round(NF, 2))
if NF>=5.0:
	print('APROVADO')
else:
	print('REPROVADO')