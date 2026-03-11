from numpy import*
a= array(eval(input(":")))
x=0
for i in a:
	if i == 1:
		x = x+80
	if i == 2:
		x = x+40
	if i == 3:
		x = x+20
	if i == 4:
		x = x+10
print(x)