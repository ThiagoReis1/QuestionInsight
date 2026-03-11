re = int(input("resultado: "))
if(re == 5):
	i = 1
	s = 5
	while(re != -1):
		re = int(input("resultado: "))
		if(re == 5):
			s = i * s
		else:
			s = s
		i = i + 1
	if(s >= 5):
		v = s / 5
		print(v)			
else:
	while(re != -1):
		re = int(input("resultado: "))
		if(re == 5):
			i = 1
			s = 5
			while(re != -1):
				re = int(input("resultado: "))
				if(re == 5):
					s = i * s
				else:
					s = s
					i = i + 1
			if(s >= 5):
				v = s / 5
				print(v)			
		
	
	
	