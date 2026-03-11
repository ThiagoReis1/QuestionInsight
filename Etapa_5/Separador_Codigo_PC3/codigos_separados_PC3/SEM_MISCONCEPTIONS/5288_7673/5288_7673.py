a = int(input())
total = 0
menores = 0
while(a > -1):
	if(menores <= 18):
		total = total + a
	   menores = total - menores
	   m = total -(menores/100) * total
		if(a <= -1):
			print(total)
	      print(round(m, 2))
   
	
	
	