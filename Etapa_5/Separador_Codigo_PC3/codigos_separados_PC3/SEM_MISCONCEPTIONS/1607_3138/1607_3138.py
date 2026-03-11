from numpy import*

vector_floor=array(eval(input("")))


i=0
floors=0
k=i

while(i<size(vector_floor) and k<size(vector_floor)):
	if(vector_floor[i]>=1 and vector_floor[i]<=20):
		floors=floors + ((vector_floor[i]-vector_floor[k]))*3
		last=((vector_floor[-2]-vector_floor[-1])*3)+floors
	i=i+1

print(last)