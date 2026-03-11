n = input().upper()
m = len(n)
i = 0
cc = 0
while(i!=m):
	if (n[i]=="H"):
		cc += 3.85
	if (n[i]=="L"):
		cc += 2.95
	if (n[i]=="E"):
		cc += 7.90
	i += 1
print(round(cc,2))