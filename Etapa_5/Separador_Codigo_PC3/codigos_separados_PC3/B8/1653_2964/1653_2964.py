import numpy as np

arrNacs = np.array(input().upper().split(','))
countNacs = np.zeros(5, dtype=int)

for i in range(0, arrNacs.size):
	if(arrNacs[i] == 'AR'):
		countNacs[0] += 1
	elif(arrNacs[i] == 'BR'):
		countNacs[1] += 1
	elif(arrNacs[i] == 'CL'):
		countNacs[2] += 1
	elif(arrNacs[i] == 'CO'):
		countNacs[3] += 1
	elif(arrNacs[i] == 'UY'):
		countNacs[4] += 1
	
print(max(countNacs))
print(countNacs)