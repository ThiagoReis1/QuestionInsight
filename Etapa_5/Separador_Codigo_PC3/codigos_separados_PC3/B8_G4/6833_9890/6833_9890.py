n=input("ESOLHA: ").upper()
i=0
p=0

while i<len(n):
	if n[i]=='M':
		p=p+7.25
	elif n[i]=='P':
		p=p+4.75
	elif n[i]=='R':
		p=p+3.50
	i=i+1
print(round(p,2))
	