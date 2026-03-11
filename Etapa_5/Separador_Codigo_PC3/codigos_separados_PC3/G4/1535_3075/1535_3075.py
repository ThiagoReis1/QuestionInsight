x = float(input())
k = int(input())
if (x< -1 or x > 1 or k <= 0):
	x = 1
	k = 1
elif (k == 1):
	arc = x
else:
	arc = x
	c = 1
	while (c < k):
		arc = arc + (-1**c)*((x**(1 + c*2))/(1 + c*2))
		c = c + 1
		
print(round(arc,6))