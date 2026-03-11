from numpy import * 
v= array(eval(input("")))
i = 0
total = 200
while i < size(v):
	if v[i] == 1:
		total = total/2
	if v[i] == 2:
		total = total*3
	if v[i] == 3:
		total = total/2
	if v[i] == 4:
		total = total*3
	if v[i] == 5:
		total = total/2
	if v[i] == 6:
		total = total*3
	i+=1
print(round(total,2))
