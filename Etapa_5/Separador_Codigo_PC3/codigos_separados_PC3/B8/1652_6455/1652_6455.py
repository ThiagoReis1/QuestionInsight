from numpy import *
etnia = input("Digite as strings: ").split(',')

q = zeros(5, dtype= int)
for i in range(size(etnia)):
	if(etnia[i] == 'B'):
		q[0] = q[0] + 1
	elif(etnia[i] == 'PA'):
		q[1] = q[1] + 1
	elif(etnia[i] == 'PR'):
		q[2] = q[2] + 1
	elif(etnia[i] == 'A'):
		q[3] = q[3] + 1
	elif(etnia[i] == 'I'):
		q[4] = q[4] + 1
print(max(q))
print(q)