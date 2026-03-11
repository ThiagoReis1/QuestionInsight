from numpy import*
x = input().upper()
i = 0
total = 0
while(i<len(x)):
	if(x[i] == "A" or x[i] == "E" or x[i] == 'I' or x[i] == 'O' or x[i] == "U"):
		total=total+ 0.19
	else:
		total = total+0.23
	i = i + 1
print(round(total, 2))