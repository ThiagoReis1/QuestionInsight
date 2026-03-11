x = int(input())
y = int(input())
n = x
s = 0
while (n<=y):
	if(n%2!=0):
		s += n
	n += 2
print(s)