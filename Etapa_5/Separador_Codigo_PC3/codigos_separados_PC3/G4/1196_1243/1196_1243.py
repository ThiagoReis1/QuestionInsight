from numpy import *
v1 = array(eval(input("Digite o vetor 1: ")))


i = 0 
count = 0
t = 60
t_2 = -60

while(i < size(v1)):
	if((v1[i] < t_2)):
		count = count + 1
	i = i + 1
i = 0
count = 0
while(i < size(v1)):
	if((v1[i] > t)):
		count = count + 1
	i = i + 1
	
v2 = array(zeros(count, dtype = float))
i = 0
count = 0
while(i < size(v1)):
	if((v1[i] >= t_2) or (v1[i] <= 60)):
		v2[count] = v1[i]
	i = i + 1


print(v1[count])
#-30.6,61.5,-100.9,-28.9,-28.5,-27.9