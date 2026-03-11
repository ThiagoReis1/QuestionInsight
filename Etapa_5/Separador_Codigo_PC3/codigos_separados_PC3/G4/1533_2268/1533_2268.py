x=float(input(": " ))
k=float(input(": " ))
t=0
while(x>=k):
	s=t + s*2/(t+1)
	t=t+1
print(round(x,8))