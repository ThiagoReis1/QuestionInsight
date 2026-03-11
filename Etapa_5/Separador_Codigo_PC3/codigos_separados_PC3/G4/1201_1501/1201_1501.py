from numpy import*
temp = array(eval(input("temperatura: ")))
i = 0
k = 0
while(i < size(temp)):
	if(temp[i] > 0 and temp[i] <= 40):
		k = k + 1
	i = i + 1
temp_2 = array(zeros(k, dtype = float))
i = 0
k = 0
while(i < size(temp)):
	if(temp[i] > 0 and temp[i] <= 40):
		temp_2[k] = temp[i]
		k = k + 1
	i = i + 1
print(temp_2)