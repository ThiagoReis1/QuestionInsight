from numpy import*
v = array(eval(input("Vetor de notas:")))
i = 0

while(i < size(v)):
	if(v[i] >= 4 and v[i] < 5):
		v[i] = 4
	if(v[i] >= 9 and v[i] < 10):
		v[i] = 10
	i = i + 1

print(v)