vt = float(input())
c = input().upper()

if c=="D" or c== "P":
	e = vt*0.11
	print(round(vt-e,2))
elif c=="C":
   e = 1
	print(round(vt-e,2))
elif c=="C":
	e = vt*0.06
	print(round(vt+e,2))