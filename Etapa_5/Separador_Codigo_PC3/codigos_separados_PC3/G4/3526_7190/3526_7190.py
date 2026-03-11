x = float(input(":"))
k = int(input(":"))

c = 0
t = 1
r = 0
while(c<k):
	r = r + x**t/t
	t = t+2
	c = c+1
	
print(round(r,7))