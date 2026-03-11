from numpy import*

temp = array(eval(input("Digite a temperatura: ")))
i = 0
j = 0 

while(i < size(temp)):
	if(temp[i]>0 and temp[i]<40):
		j = j + 1
	i = i + 1

temp1 = array(zeros(j, dtype =  float))
i = 0
j = 0

while(i < size(temp)):
	if(temp[i]>0 and temp[i]<40):
		temp1[j] = temp[i]
		j = j + 1
	i = i + 1
print(temp1)