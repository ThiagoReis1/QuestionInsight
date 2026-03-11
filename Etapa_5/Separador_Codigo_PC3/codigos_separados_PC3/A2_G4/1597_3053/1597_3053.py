from numpy import*
v = array(eval(input("Valores: ")))

i = 0
g = 0
soma = sum(v)

while(i < size(v)):
	if (v[i] > 80):
		g = g + 1
	else:
	   g = g
	i = i + 1
if (g>=1):
	soma = soma - 5
else:
	soma = soma
print(round(soma , 2))

