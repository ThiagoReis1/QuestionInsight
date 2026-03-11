from numpy import*
ev= input("Nacionalidade: ").split(',')
z= zeros(5, dtype=int)
for i in range(size(ev)):
	if(ev[i] == "AR"):
		z[0] += 1
	elif(ev[i] == "BR"):
		z[1] += 1
	elif(ev[i] == "CL"):
		z[2] += 1
	elif(ev[i] == "CO"):
		z[3] += 1
	else:
		z[4] += 1
		
print(max(z))
print(z)
