from numpy import*

saq = array(eval(input(":")))
var = 0

for i in range (size(saq)):
	if saq[i] >= 2000:
		var[i] += 1
print(saq)