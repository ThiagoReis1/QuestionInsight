#Universidade Federal do Amazonas
#Thiago Tuma Camilo 21600549
from numpy import *
temp = array(eval(input("Digite as temperaturas encontradas:")))
i = 0 #variavel contadora
k = 0 #variavel acumuladora
while(i < size(temp)):
	if(temp[i] > -60 and temp[i] < 60):
		k = k + 1
	i = i + 1

temp2 = array(zeros(k, dtype = float))
i = 0
k = 0
while(i < size(temp)):
	if(temp[i] > -60 and temp[i] < 60):
		temp2[k] = temp[i]
		k = k + 1
	i = i + 1
print(temp2)