oq=str(input(""))
total=0
i=0
a=0
l=0
p=0
while i< len(oq):
	if oq[i].upper() == "A":
		total= total + 19.90
		a=a+ 1
	elif oq[i].upper() == "L":
		total= total + 3.50
		l=l+1
	elif oq[i].upper() == "P":
		total= total + 4.25
		p=p+1
	i= i+ 1
print(round(total, 2), a, l, p)