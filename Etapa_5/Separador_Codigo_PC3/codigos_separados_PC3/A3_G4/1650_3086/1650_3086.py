from numpy import*
x = input().split(',')
a = 0
y = zeros(5,dtype=int)
for i in x:
	if(i == "P"):
		y[0]= y[0] + 1
	if(i== "C"):
		y[1]=y[1] + 1
	if(i== "R"):
		y[2]= y[2] + 1
	if(i== "L"):
		y[3]=y[3] + 1
	if(i== "B"):
		y[4]= y[4] + 1
print(max(y))
print(y)