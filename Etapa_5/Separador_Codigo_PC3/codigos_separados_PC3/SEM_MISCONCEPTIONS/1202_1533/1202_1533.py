from numpy import*
v = array(eval(input("Pesagem?: ")))
i = 0
k = 0
t = 40
while(i < size(v)):
	if (v[i] > t):
		k = k+1
	i = i+1
v2 = array(zeros(k, dtype = float)