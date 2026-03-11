x= float(input("x?"))
k= int(input("k?"))
t=1
s=0
q=0
u=0
j=k-q

while(j!=0):
	u=((-1)**q)*(x**t)/t
	t=t+2
	q=q+1
	s=s+u
	j=k-q
print(round(s,6))