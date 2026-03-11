from numpy import*
v = array(eval(input()))
i = 0
c = 1
soma = 0

while(c < size(v)):
	aa = int(v[i])
	a = int(v[c]) - aa
	a = (a ** 2) ** (1/2)
	soma = soma + a
	i = i + 1
	c = c + 1
print(int(soma))