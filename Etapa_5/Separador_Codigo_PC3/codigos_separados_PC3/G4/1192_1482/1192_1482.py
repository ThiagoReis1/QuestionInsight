#Thaynara Marques
#ap5
from numpy import*
temp = array(eval(input("digite as temperaturas:")))
i = 0
np = 0
while (i<size(temp)):
	if (temp[i]>=0):
		np = np+1
	i = i+1
temp2 = array(zeros(np, dtype = float))
i = 0
np = 0
while (i<size(temp)):
	if (temp[i]>=0):
		temp2[np] = temp[i]
		np = np+1
	i = i+1
print (temp2)