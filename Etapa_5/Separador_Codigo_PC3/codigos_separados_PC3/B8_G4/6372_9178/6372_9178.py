from numpy import*

x = input("Entrada: ").upper().split(',')

j=zeros(4,dtype = int) 


for i in range(len(x)):
	
	if x[i]== 'A':
		j[0] += 1

	elif x [i]== 'B':
		j[1] += 1

	elif x[i] == 'L':
		j[2] += 1

	elif x[i] == 'H':
		j[3] += 1
	
print(j)
	

