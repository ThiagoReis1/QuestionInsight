a=input()
i=0
s=100
while i<len(a):
	if a[i]=="1":
		s=s*5
	elif a[i]=="2":
		s=s*3
	elif a[i]=="3":
		s=s
	elif a[i]=="4":
		s=s/2
	i=i+1
print(round(s,2))