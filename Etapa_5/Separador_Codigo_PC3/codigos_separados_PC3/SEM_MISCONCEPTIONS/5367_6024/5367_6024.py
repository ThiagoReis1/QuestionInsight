from numpy import *
cpf = array(eval(input("digite o cpf: ")))
extra = [1,2,3,4,5,6,7,8,9]
i = 0
total_soma = 0
while i<len(cpf):
	total_soma = total_soma + (cpf[i]*extra[i])
	i = i + 1
#Total_soma = cpf[0]*extra[0]+cpf[1]*extra[1]+cpf[2]*extra[2]+cpf[3]*extra[3]+cpf[4]*extra[4]+cpf[5]*extra[5]+cpf[6]*extra[6]+cpf[7]*extra[7]+cpf[8]+extra[8]+cpf[9]*extra[9]
resto = total_soma % 11
print(resto)