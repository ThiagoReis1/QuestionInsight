from numpy import* 
temp = array(eval(input("Informe as temperaturas: ")))
i = 0
j = 0
while(i<size(temp)):
	if(temp[i]<60 and temp[i]>-60):
		j = j+1
	i = i+1
temp1 = array(zeros(j, dtype = float))
i = 0
j = 0
while(i<size(temp)):
	if(temp[i]<60 and temp[i]>-60):
	   temp1[j]  = temp[i]
	   j = j+1
	i = i+1
print(temp1)
