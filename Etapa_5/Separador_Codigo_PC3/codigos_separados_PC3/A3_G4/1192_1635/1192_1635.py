from numpy import*
v = array(eval(input("digite a temperatura: ")))
i = 0
j = 0
s = size(v) 
while(i < size(v)):
	if(v[i] < 0):
		j = j + 1
	i = i + 1
	
s = size(v) - j
v2 = array(zeros(s, dtype = float))
i = 0
k = 0
while(i < size(v)):
	if(v[i] > 0):
		v2[k] = v[i]
		k = k + 1
	i = i + 1
print(v2)
