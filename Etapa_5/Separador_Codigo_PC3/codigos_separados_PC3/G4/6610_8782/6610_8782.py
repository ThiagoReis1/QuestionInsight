n=int(input("numero: "))
c=1
s=0
while c <= n:
	if c%2==0:
		s=s+c
	c+=1
print("soma=",s)