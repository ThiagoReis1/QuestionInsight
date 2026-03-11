n=float(input())
k=int(input())

i=0
j=3
tot=n
while(i!=k-1):
	tot=tot+(n**j)/j
	j=j+2
	i=i+1
print(round(tot,7))