from numpy import*
v1 = array(eval(input("Digite o peso do levantamento:")))
i = 0
k = 0
r = 217
while (i < size(v1)):
	if (v1[i] > r):
		k = k + 1
	i = i + 1
print(r)
print(k)