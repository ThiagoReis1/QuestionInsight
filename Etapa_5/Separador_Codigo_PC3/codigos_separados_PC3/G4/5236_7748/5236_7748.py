num= int(input('num:'))

x= num%3 
y= num%5
z= num%5 + num%3

if x==0 and y!=0:
	print('Pirlim')
	
else:
	if y==0 and x!=0:
		print('Pimpim')
	
	else:
		if z==0:
			print('PirlimPimpim')
		
		else:
			print(num)