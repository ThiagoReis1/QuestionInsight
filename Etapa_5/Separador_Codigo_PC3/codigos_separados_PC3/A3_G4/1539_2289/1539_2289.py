x = float(input())
k = int(input())

soma = 0
p = 0

while (-1 < x < 1 and k > 0 and p < k):
	c = ((-1)**(p+1)) * (x**(p + 1)) + 1
	p = p + 1
print(round(c, 7))