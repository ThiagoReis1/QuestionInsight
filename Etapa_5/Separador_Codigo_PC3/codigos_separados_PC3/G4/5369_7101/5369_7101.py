from numpy import*
v = array(eval(input("Digite seu CPF: ")))
i = 0
j = 9
t = 0
while (i<size(v)):
	t = t + (v[i]*j)
	i = i + 1
	j = j - 1
print(t%11)