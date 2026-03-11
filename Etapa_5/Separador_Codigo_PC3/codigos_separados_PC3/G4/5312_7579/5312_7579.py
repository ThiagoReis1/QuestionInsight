n = int(input(":"))
h = int(input(":"))

while h > 0:
	por = int(n * 0.02)
	n = n + por
	h = h - 1
	
print(n)