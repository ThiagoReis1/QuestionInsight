#LETICIA DANTAS - 21601436

from numpy import*

temp = array(eval(input("Qual a temperatura? ")))
i = 0
j = 0
while(i < size(temp)):
	if(temp[i] >= 10):
		j = j + 1
	i = i + 1

temp2 = zeros(j, dtype = float)
i = 0
j = 0
while(i < size(temp)):
	if(temp[i] >= 10):
		temp2[j] = temp[i]
		j = j + 1
	i = i + 1
print(temp2)