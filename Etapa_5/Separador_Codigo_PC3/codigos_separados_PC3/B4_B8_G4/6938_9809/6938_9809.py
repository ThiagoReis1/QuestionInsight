v = float(input())
c = input().upper()
if (c=="D"):
	d = v*0.11
	v -= d
elif (c=="P"):
	d = v*0.11
	v -= d
elif (c=="C"):
	q = int(input())
	if (q==2):
		j = v*0.06
		v += j
print(round(v,2))