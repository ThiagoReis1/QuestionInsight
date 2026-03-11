cc = float(input())
if (cc > 0) and (cc < 17.5):
	total = cc + 10.5
	print (round(total, 2))
elif (cc >= 17.5) and (cc < 35):
	total = cc + 14.0
	print (round(total,2))
elif (cc >= 35.0) and (cc < 50):
	total = cc + 18.6
	print (round(total,2))
else:
	total = cc + 24.5
	print (round(total,2))