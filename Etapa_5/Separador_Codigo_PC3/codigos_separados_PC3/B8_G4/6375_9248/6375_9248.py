from numpy import*
a = input('ns: ').split(',')
b = zeros(4, dtype=int)


for i in a:
	if(i == 'A'):
		b[0] += 1
	elif(i == 'B'):
		b[1] += 1
	elif(i == 'C'):
		b[2] += 1
	elif(i == 'D'):
		b[3] += 1
		
print(b)