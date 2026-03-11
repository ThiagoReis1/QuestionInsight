from numpy import * 
y = zeros(6, dtype = int)
x = input(":").upper().split(',')
cont = 0
for i in x:
	if (i == 'MC'):
		y[0] += 1
	elif (i == 'C'):
		y[1] += 1
	elif (i == 'CM'):
		y[2] += 1
	elif (i == 'EM'):
		y[3] += 1
	elif (i == 'E'):
		y[4] += 1 
	elif (i == 'ME'):
		y[5] += 1

print(max(y))
print(y)