from numpy import*
x = input().split(',')
a = 0
y = zeros(5, dtype = int)
for i in x:
	if(i == "AC"):
		y[0] = y[0] + 1
	elif(i == "AM"):
		y[1] = y[1] + 1
	elif(i == "PA"):
		y[2] = y[2] + 1
	elif(i == "RO"):
		y[3] = y[3] + 1
	elif(i == "RR"):
		y[4] = y[4] + 1
		
print(max(y))
print(y)