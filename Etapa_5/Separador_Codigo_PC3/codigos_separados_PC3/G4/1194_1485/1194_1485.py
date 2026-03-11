from numpy import*
v = array(eval(input("digite os valores: ")))
i = 0
n = 0
s = 0
while (i < size(v)):
	if (v[i] > -100 ):
		n = n +1
	i = i + 1
v2 = array(ones(n, dtype = float))
i = 0 
while (i < size(v)):
	if(v[i] > -100):
		v2[s]=v[i]
		s = s + 1
	i = i + 1
print (v2)