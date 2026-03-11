a = 19.9
l = 3.5
p = 4.25

total= [0,0,0]
soma= 0
entrada = input()
i =0 
while(i<len(entrada)):
	if(entrada[i].upper()=='A'):
		soma+=a
		total[0]+=1
	elif(entrada[i].upper()=='L'):
		soma+=l
		total[1]+=1
	elif(entrada[i].upper()=='P'):
		soma+=p
		total[2]+=1
	i+=1
print(round(soma,2))
i=0
while(i<len(total)):
	print(total[i])
	i+=1
