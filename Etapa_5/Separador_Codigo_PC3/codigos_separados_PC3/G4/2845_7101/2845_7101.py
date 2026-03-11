from numpy import*
v = array(eval(input("Digite o codigo: ")))
for i in range(size(v)):
	if (0<=v[i]<=8):
		v[i] = v[i] + 1
	else:
		v[i] = 0
print(v)