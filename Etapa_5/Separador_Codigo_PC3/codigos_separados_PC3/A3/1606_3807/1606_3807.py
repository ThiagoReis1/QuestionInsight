from numpy import*

a = array(eval(input("andares que parou:")))
c = 1
andares = 20
total = 0

while (c < size(a)):
	total = total + abs(a[c] - a[c-1])
	c = c + 1
	
print(total)





