from numpy import*
n = array(eval(input("")))
i = 0
j = 1
k = 0 
soma = 0
while (i < size(n)):
	soma = (n[i]*j) + soma
	k = k + j
	j = j + 1
	i = i + 1
print(round(soma/k,2))


