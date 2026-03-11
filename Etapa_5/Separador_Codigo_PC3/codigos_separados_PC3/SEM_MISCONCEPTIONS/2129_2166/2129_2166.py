from numpy import *
nota= array(eval(input("media final do aluno: ")))
pesos=[1.0,2.0,3.0,4.0]

i=0
soma=0
while(i<size(nota)):
	soma=soma+nota[i]*pesos[i]
	i=i+1
media=round(soma/10,2)
print(media)
if(media >= 5):
	print("APROVADO")
else:
	print("REPROVADO")