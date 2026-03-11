z = int(input())
h = int(input())
x = int(input())
y = int(input())
i = 0

while h > 0:
	h = h - x*z
	z = z + x*z 
	z = z-y
	i += 1
print(i)