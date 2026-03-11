from numpy import*

v = input()
v1 = v.split(";")



cont = zeros(5, dtype=int)

for i in range(size(v)):
	if(v1[i] == 'P'):
		cont[0] = cont[0] + 1
	elif(v1[i] == 'C'):

		cont[1] = cont[1] + 1
	elif(v1[i] == 'R'):
	
		cont[2] = cont[2] + 1
	elif(v1[i] == 'L'):
		
		cont[3] = cont[3] + 1
	elif(v1[i] == 'B'):
		
		cont[4] = cont[4] + 1
print(max(cont))
print(cont)