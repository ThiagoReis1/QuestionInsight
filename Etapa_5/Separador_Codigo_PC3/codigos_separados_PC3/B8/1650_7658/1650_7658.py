from numpy import *
tc=input('P,C,R,L OU B?').upper().split(',')
cores= zeros(5, dtype= int)
for i in range(size(tc)):
	if tc[i] == 'P':
		cores[0] = cores[0] + 1
	elif tc[i] == 'C':
		cores[1] = cores[1] + 1
	elif tc[i] == 'R':
		cores[2] +=1
	elif tc[i] == 'L':
		cores[3] += 1
	elif tc[i] == 'B':
		cores[4] += 1
print(max(cores))
print(cores)
