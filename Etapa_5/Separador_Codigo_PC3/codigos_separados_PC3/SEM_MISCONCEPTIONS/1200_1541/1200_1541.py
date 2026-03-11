from numpy import*
temp= array(eval(input("temperaturas:")))
i=0
j=0
while(i<size(temp)):
	if(temp[i]>10 and temp[i]<40):
		j= j+1
	i= i +1
temp1= array(zeros(j, dtype =float))
i=0
j=0
while(i<size(temp)):
	if(temp[i]>10) and 
		