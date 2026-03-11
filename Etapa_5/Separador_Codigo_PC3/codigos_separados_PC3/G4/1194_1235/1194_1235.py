from numpy import*
v1= array(eval(input("Digite o vetor: ")))
i=0
count=0
t = -100
while(i < size(v1)):
	if(v1[i] > t):
		count = count + 1
	i = i + 1
v2= array(zeros(count, dtype = float))
i = 0
count = 0
t = -100
while(i < size(v1)):
	if(v1[i] > t):
		v2[count] = v1[i]
		count = count + 1
i = i + 1
print(v2)