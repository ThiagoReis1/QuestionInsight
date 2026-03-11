altura_luna = 1.65
taxa_luna = 0.02

c=float(input("crescimento : "))
t=float(input("taxa: "))
n=0

while c < altura_luna:
	altura_luna=altura_luna + taxa_luna
	c=c+t
	n=n+1
print(n)
	

