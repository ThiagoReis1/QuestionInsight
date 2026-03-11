from numpy import*
x = array(eval(input()))
i = 0
total = 0

while(i<size(x)):
	if(x[i] > 160):
		
		total = total+ x[i]-25
	else:
		total = total+ x[i]
	i = i + 1
print(round(total, 2))