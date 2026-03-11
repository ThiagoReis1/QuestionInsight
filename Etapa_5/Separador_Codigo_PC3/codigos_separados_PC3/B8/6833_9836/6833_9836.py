from numpy import*
var=input("insira:")
i=0
total=0
while i < len(var):
	if var[i] == 'M':
		total += 7.25
	elif var[i] == 'P': 
		total += 4.75
	elif var[i] == 'R':
		total += 3.50
	i += 1
print(round(total,2))
	
