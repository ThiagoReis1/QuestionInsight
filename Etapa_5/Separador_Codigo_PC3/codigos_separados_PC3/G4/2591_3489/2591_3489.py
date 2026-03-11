from numpy import*

v =array(eval(input("insira o vetor :")))
x = 0
for i in range(size(v)):
	if (v[i]>= v[0]):
		x = x + 1
		v[i] = v[i] + 1
print(i)
print(x)
print(v[i])
