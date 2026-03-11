v = float(input())
c = input()
if c == "D" or c == "P":
	vf = v*0.88
elif c == "C":	
	p = int(input())
	if p == 1:	
		vf = v	
	elif p == 2:	
		vf = v*1.07
else:	
	print()	
	exit()
print(round(vf, 2))