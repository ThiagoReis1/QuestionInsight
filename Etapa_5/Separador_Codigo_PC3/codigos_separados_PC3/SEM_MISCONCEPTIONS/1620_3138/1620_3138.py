from numpy import*
vector_time=array(eval(input("")))
vector_percent=array(eval(input("")))

i=0
j=0
new=0

	
while(i<size(vector_time)and j<size(vector_percent)):
	if(vector_time[i]!=0 and vector_percent[j]!=0):
		percent=(vector_percent[i]*5)/(100)
		new=new+percent*vector_time[i]
	i=i+1
	j=j+1
print(new)
	
	
	
