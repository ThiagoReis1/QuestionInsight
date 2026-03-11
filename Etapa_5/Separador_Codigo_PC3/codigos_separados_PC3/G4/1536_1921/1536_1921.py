x = int(input())
k = int(input())
indice = 2
i = 1
s = 1
while(i <= k):
	
	if(indice % 2 != 0):
		s = s - (x**indice)/indice
		
	else:
		s = s + (x**indice)/indice
	indice = indice + 1
	i = i + 1 
print(round(s,10))