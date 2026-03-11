z = int(input("quantos zumbis tem?"))
h = int(input("quantos seres humanos restam?"))
x = int(input("quantos humanos um zumbi é capaz de matar por dia?"))
y = int(input("quantos zumbis os humanos conseguem matar por dia?"))
i = 0

while (h > 0): 
	z = (z * x)
	z = z - y
	h = h - z
	i = i + 1
	
print(i)