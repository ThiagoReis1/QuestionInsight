from numpy import *
ev = input(",").split(',')
z = zeros(5, dtype =int)
for i in range(size(ev)):
	if(ev[i] == "AM"):
		z[0] += 1
	elif(ev[i] == "PE"):
		z[1] += 1
	elif(ev[i] == "MG"):
		z[2] += 1
	elif(ev[i] == "SP"):
		z[3] += 1
	else: 
		z[4] += 1
		
print(max(z))
print(z)