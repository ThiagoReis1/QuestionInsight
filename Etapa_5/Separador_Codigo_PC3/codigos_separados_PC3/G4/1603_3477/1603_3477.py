from numpy import*
j =  array(eval(input("numero a qual acerto: ")))
i = 0
anel = 0
while(i < size(j)):
	if(j[i] == 80)  and (j[i] == 40 ) and (j[i] == 20 ):
		anel = anel + 1
	i = i+1		
print(i)	
