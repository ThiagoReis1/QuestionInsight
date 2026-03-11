from numpy import*
onibus=array(eval((input())))
i=0
total=0
while(i<size(onibus)):
	if(total<76):
		total=total+onibus[i]
		
	elif(i==(size(onibus)-1) and (total+onibus[i]>75)):
		total=75
	else:
		total=75+onibus[i]
	
	i=i+1

print(total)