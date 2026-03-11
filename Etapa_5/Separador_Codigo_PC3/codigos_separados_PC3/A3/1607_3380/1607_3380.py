from numpy import *

v1 = array(eval(input()))
vet_andares = array(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12','13','14','15','16','17','18','19','20'])
i = 0
j = 1
maior = max(v1)
while v1[i] < size(v1) :
	soma= (v1[i] - v1[i+1]) * 3
	soma= soma +1
	i = i + 1
print(soma)