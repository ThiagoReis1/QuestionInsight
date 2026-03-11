di= float(input('deposito inicial porra: '))
m= int(input('meses de aplication: '))
total= di
i= 0

while(i<m):
	total= total+total*0.012
	i= i+1
	print(round(total, 2))