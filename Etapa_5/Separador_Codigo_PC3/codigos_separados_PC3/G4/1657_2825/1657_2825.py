from numpy import*
x = input("").split(',')
y = array([0,0,0,0,0])

for elemento in x:
	if(elemento == "AZ"):
		y[0] = y[0] + 1
	if(elemento == "CA"):
		y[1] = y[1] +1
	if(elemento == "FL"):
		y[2] = y[2] +1
	if(elemento == "PA"):
		y[3] = y[3]+1
	if(elemento == "WI"):
		y[4] = y[4] +1
print(max(y))
print(y)