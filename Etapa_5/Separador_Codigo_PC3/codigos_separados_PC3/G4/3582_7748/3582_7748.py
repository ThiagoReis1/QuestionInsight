from numpy import*

ci= array(eval(input('ci:')))

i=0
while(i<size(ci)):
	if(ci[i]>160):
		ci[i]= ci[i]-25
	
	i=i+1
print (round(sum(ci),2))
		
	
		
	
		
		
		
		