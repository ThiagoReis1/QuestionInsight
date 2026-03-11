from numpy import*
v = array(eval(input("Vetor:")))

c = 0
while(c < size(v)):
	if(v[c]== min(v)):
		a = c
	c = c + 1
print(a)