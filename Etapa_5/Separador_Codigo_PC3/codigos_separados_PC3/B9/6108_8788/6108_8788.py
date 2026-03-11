qnt = float(input())

if qnt < 17.5:
	total = qnt + 1.5
elif qnt >= 17.5 and qnt < 35:
	total = qnt + 2.3
elif qnt >= 35 and qnt < 50:
	total = qnt + 3.3
else:
	total = qnt + 4.7
	
print(round(total,1))
	