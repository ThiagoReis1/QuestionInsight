i= int(input(""))
c= int(input(""))
pi = float(input(""))
pc = float(input(""))

t=0
while(i+c < 50000):
	i = (i*pi/100) + i
	c = (c*pc/100) +c
	t=t+1
print(t)