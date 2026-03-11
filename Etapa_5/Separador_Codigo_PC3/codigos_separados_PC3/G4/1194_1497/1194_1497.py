from numpy import*
v = array(eval(input("")))
i = 0
tam = 0
while (i < size(v)):
	if(v[i] > -100):
		tam = tam + 1
	i = i + 1

v2 = zeros(tam, dtype = float)
i = 0
j = 0

while(i < size(v)):
	if(v[i] > -100):
		v2[j] = v[i]
		j = j + 1
	i = i + 1
print(v2)