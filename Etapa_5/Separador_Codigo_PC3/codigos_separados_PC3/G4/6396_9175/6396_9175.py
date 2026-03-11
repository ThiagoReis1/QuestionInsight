from numpy import*
v = array(eval(input("Digite um numero: ")))

for i in range(size(v)):
	v[i]= 2 * v[i]

print(v)
