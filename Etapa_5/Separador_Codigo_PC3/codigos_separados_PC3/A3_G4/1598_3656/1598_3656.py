from numpy import*
c = array(eval(input("valor de cada item: ")))
co = 0
s = 0
while (size(c) > co):
	if (c[co] > 80):
		c -= 5 
	co +=1
total = sum(c)
print (round(total,2))