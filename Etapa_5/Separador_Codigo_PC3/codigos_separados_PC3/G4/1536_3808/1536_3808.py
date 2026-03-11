x = float(input())
k = int(input())
i = 0
serie = 0
while (i<k):
   if x<=1 and x>-1:
	   t =(x**(i+1))*((-1)**(i))/(i+1)
	   serie = serie + t
	   i = i + 1
print(round(serie, 10))
		
		
