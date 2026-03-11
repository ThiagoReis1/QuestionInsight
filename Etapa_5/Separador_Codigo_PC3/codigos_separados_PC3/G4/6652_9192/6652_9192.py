from numpy import*

n = array(eval(input("Informe a nota: ")))
p = [2,2,6,1]

i = 0
soma = 0
while(i < size(n)):
	soma = soma + n[i] * p[i]
	i = i + 1
	
print(round(soma/sum(p),2))