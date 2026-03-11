a=float(input())
b=int(input())

j=a
i=0

while i<b:
	j=j-(j*0.05)
	i=i+1
	print(round(j,2))
