from  numpy import*

a = input("strig: ").upper()
i = 0

b = 0
c = 0

while(i < len(a)):
	if(a[i] == "A" or a[i] == "E" or a[i] == "I" or a[i] == "O" or a[i] == "U"):
		b = b + 0.15
	
	else:
		c = c + 0.17
	
	i = i + 1

print(round(sum(b) + sum(c), 2))