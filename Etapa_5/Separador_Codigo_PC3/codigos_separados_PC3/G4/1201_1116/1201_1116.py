from numpy import*
v1 = array(eval(input("Informe as temperaturas :")))
i = 0
k = 0
while(i < size(v1)):
	if(v1[i] > 0 and v1[i] < 40):
		k= k+1
	i = i+1
v2 = array(zeros(k,dtype = float))
j= 0
x = 0
while(j < size(v1)):
	if(v1[j] > 0 and v1[j] < 40):
		v2[x] = v1[j]
		x = x+1
	j = j +1
print(v2)	