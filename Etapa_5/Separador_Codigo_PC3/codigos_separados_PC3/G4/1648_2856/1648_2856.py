from numpy import*
v = array(eval(input("v: ")))
c = 0
i = 0

while(i < size(v)):
	if(v[i] < 70):
		c = c + 1
	i = i + 1
	
x = zeros(c, dtype = int)

i = 0
a = 0
while(i < size(v)):
	if(v[i] < 70):
		x[a] = i
		a = a + 1
		
	i = i + 1

print(c)
print(x)	