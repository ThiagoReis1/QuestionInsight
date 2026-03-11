from numpy import*
v = array(eval(input("digite o valor: ")))
a = 0
for i in range(size(v)):
	if(v[i]< v[0]):
		a = a + 1
	if(v[i] < v[0]):
		print(i)
print(a)
		