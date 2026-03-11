from numpy import *
p = array(eval(input("peso dos alunos: ")))
a= array(eval(input("altura dos alunos: ")))
imc= ones(size(p))
situacao= ""
for i in range(size(p)):
	imc[i]= round(p[i]/(a[i]**2),2)
print(imc)
if(max(imc) < 17):
	situacao= "MUITO ABAIXO DO PESO"
elif(17 <= max(imc) <= 18.49):
	situacao="ABAIXO DO PESO"
elif(18.5 <= max(imc) <= 24.99):
	situacao= "PESO NORMAL"
elif(25 <= max(imc) <= 29.99):
	situacao= "ACIMA DO PESO"
elif(30 <= max(imc) <= 34.99):
	situacao= "OBESIDADE"
elif(35 <= max(imc) <= 39.99):
	situacao= "OBESIDADE SEVERA"
else:
	situacao= "OBESIDADE SEVERA"
print("O MAIOR IMC DA TURMA EH:",max(imc),situacao)
