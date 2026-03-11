from numpy import *
temp = array(eval(input("temperaturas:")))
i = 0 
j = 0
while(i < size(temp)):
	if (temp[i] > 22):
		j = j + 1
	else:
		i = i + 1
i = 0
j = 0
temp2 = array(zeros(j,dtype = float))
while(i < size(temp)):
	if(temp[i] > 22):
		temp2[j] = temp[i]
		j = j + 1
	i = i + 1	
print(temp2)	