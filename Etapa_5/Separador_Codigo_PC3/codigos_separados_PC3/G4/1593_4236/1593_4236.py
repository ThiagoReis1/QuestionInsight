from numpy import*
n = array(eval(input(" ")))
tam = size(n)
soma = 0
i = 0
p = 1
while (i < tam):
	soma = soma + n[i]*(p) 
	i = i + 1
	p = p + 1
media = soma/p
print(round(media, 2))