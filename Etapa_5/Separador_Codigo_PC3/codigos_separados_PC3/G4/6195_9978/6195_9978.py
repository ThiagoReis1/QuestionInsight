n = int(input("numero: "))
t = int(input("taxa: "))
b = n
c = 0
while b < n*2:
	b += (t/100)*b
	c = c+ 1

print(c)



