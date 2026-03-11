from numpy import*
temp = array(eval(input("Informe as temperaturas: ")))
i = 0
j = 0
while(i<size(temp)):
	if(temp[i]<50):
		j = j+1
	i = i+1	
templ = array(zeros(j, dtype = float))
i = 0
j = 0
while(i<size(temp)):
	if(temp[i]<50):
		templ[j] = temp[i]
		j = j+1
	i = i+1
print(templ)	