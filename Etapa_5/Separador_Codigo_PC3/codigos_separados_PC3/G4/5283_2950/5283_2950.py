n = int(input())

i = 0
t = 0

while (n != 0):
	if (n >= 1):
		t = t + 1
	n = int(input())
	i = i + 1
		
p = (t/i)*100

print(i)
print(round(p,2))