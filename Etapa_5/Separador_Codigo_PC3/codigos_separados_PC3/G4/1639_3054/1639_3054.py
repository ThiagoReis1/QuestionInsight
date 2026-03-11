from numpy import*

v = array(eval(input("vetor: ")))
cont = 0

for i in range(size(v)):
	if(v[i]%2==0):
		cont = cont + 1
print(cont)

t = zeros(cont, dtype = int)
k = 0

for i in range(size(v)):
	if(v[i] % 2==0):
		t[k] = i
		k = k + 1
print(t)		

	