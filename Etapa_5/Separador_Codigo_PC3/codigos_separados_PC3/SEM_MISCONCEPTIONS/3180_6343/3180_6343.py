from numpy import * 
n = array(eval(input("n: ")))
total = zeros(n, dtype=int)
for i in range(shape(n)[0]):
	if i == 0:
		total[0] = total[0] + 1
	elif i == 1:
		total[1] = total[1] + 1	
	elif i == 2:
		total[2] = total[2] + 1
	elif i == 3:
		total[3] = total[3] + 1
	elif i == 4:
		total[4] = total[4] + 1
	else:
		total[5] = total[5] + 1
print(total)