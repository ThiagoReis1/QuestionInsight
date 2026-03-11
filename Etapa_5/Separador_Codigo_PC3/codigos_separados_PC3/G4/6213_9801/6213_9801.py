N = int(input("N? "))

c = 0

while N != -1:
	if N >= 101 and N <= 201:
		c = c + 1
	N = int(input("N? "))
print(c)