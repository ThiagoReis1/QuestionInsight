x=float(input("x?"))
k=float(input("k?"))
t=0
s=0
j=k
u=0
while(j!=0):
	u=(x  **  t)*( -1  **  t)
	t=t+1
	j=k-t
	s=s+u
print(round(s,7))