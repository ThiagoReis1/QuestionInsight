tx = 5
t = float(input())
if (t<2):
	tx += 1.25
elif (t==2):
	tx += 2.25
else:
	tx += 3.25
print(round(tx,2))