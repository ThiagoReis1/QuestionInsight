x = float(input("real"))
k = int(input("quantidade"))
i =1
s=0
while(i<=k):
	s=s+x**(2*i-2)*(-1)**(i-1)
	i=i+1
print(round(s,8))	