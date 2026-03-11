from numpy import* 

n = array(eval(input("digite")))
p = 100
i = 0 
while(i<size(n)):
	if (n[i]== 1):
		p += p*5
		i+=1
	elif (n[i]== 2):
		p += p*3
	
		i+=1
	elif (n[i]== 3):
		p = p

		i+=1
	elif (n[i]== 4):
		p += p/2
		
	i+=1
print(round(s,2))
