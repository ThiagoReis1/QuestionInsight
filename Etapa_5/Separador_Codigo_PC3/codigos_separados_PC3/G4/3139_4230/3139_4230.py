from numpy import*
v = array(eval(input("")))
tam = size(v)
i=0
soma=0
while(i<tam):
	soma = soma + v[i]**(1/3)
	i = i + 1
media = (soma/tam)**3
print(round(media,2))