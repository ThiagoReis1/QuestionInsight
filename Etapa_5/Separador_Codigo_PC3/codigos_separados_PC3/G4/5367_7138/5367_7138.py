from numpy import*

cpf = array(eval(input()))
ex = [1,2,3,4,5,6,7,8,9]

i = 0

while(i < size(cpf)):
	cpf[i] = cpf [i] * ex[i]
	i = i + 1
print(sum(cpf)%11)