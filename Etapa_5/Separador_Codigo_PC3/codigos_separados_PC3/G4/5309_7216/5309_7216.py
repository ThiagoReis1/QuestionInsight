x = float(input())
k=int(input())

S=x
d=3
i=0

while(i+1<k):
	S=S+x/d
	d=d+2
	i=i+1
	
print(round(S,8))
	