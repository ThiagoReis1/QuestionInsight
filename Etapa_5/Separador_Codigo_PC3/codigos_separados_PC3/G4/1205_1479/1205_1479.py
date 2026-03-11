#LETICIA DANTAS - 21601436

from numpy import*

d = array(eval(input(" Qual a distancia?")))
i = 0
j = 0
r = 8.95
while(i < size(d)):
	if(d[i] > r):
		j = j + 1
	i = i + 1
print(r)
print(j)