x=float(input("x:"))
k=int(input("k:"))

i=1
r=1

while(i!=k):
	r=r+((-1)**(i))*(x**i)
	i=i+1
print(round(r,7))