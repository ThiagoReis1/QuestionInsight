n = int(input("numero:"))
t = int(input("taxa:"))
b = n
c = 0
while b < 2*n :
	c = c + 1 
	b = b+b*(t/100)
print(c)