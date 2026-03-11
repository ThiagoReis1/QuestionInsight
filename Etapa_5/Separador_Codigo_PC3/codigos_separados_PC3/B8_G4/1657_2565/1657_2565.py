from numpy import*

vet = input("estado: ").split(',')
e = array(["AZ", "CA", "FL", "PA", "WI"])

b = array([0,0,0,0,0])


for i in (vet):
	if(i == e[0]):
		b[0]  += 1
	elif(i ==e[1]):
		b[1] += 1
	elif(i == e[2]):
		b[2] += 1
	elif(i == e[3]):
		b[3] += 1
	elif(i == e[4]):
		b[4] += 1
	
print(max(b))
print(b)

		
	
	

