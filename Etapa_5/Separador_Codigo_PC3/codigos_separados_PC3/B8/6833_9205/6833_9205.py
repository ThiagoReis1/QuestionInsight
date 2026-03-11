produtos= input().upper()
i=0
total = 0.0
while(i < len(produtos)):
	pro = produtos[i]
	if(pro == 'M'):
		total+= 7.25
	elif(pro=='P'):
		total+=4.75
	elif(pro=='R'):
	   total+=3.50
	i+=1
print(round(total,2))