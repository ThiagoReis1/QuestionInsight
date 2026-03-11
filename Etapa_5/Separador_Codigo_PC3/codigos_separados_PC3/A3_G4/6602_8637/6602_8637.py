# faça seu código aqui!

n=int(input())
qt=input().upper
c=0
l=1
i=1
p=1

while c<n:
	qt=input().upper
while c<n:
	if n=="L" or n=="C" or n=="P":
		if n== "L":
			l=l+1
			c=c+1
		if n== "C":
			i=i+1
			c=c+1
		if n=="P":
			p=p+1
			c=c+1
	qt=input().upper
print(c)


