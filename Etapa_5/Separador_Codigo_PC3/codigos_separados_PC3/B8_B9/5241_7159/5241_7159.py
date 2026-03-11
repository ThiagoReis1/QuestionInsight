c = int(input())

if(c < 10):
	total = c*2 + 20
	print(round(total,2))
elif(c >= 10 and c < 20):
	total = c*2.5 + 20
	print(round(total, 2))
elif(c >= 20 and c < 40):
	total = c*2.75 + 20
	print(round(total,2))
elif(c >= 40):
	total = c*3 + 20
	print(round(total,2))