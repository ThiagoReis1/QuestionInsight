n = int(input())

cont= 0
contpar = 0
 
while(n!=0):
	if (n%2 ==0 ):
		contpar = contpar + 1
	else:
		cont = cont + 1
	n = int(input())
	
total = cont+contpar
perc = contpar*100/total
print(total)
print(round(perc,2))
	