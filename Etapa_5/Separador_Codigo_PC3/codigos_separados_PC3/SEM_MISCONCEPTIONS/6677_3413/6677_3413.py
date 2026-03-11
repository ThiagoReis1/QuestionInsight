import numpy as np

count = 0
var = []
while count < 10:
	aux = float(input())
	if(aux >= 0 and aux <= 20):
		var.append(aux)
		count += 1
		
count = int(input())

result = []
for i in var:
	if(i>= count):
		result.append(i)
		
print(len(result))
print(np.array(result))