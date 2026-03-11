from numpy import*
v = array(eval(input("Vetor:")))

c = 1
total = 0

while (c < size(v)):
	total = total + abs(v[c]-v[c-1])
	c = c + 1
print(total)