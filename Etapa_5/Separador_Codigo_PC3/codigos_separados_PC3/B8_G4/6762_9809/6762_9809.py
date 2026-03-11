i = int(input())
c = 20
if (i<12):
	c+=1.25
elif (i==12):
	c+=2.25
elif (i>12):
	c+=3.25
print(round(c,2))