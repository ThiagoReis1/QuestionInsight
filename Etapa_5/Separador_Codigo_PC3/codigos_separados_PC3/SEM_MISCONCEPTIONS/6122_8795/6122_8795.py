x=int(input("quantidade: "))
if x<17.5:
	total=x+0.8
	print(round(total,2))
elif 17.5<=x<=35.0:
	total=x+1.3
	print(round(total,2))
elif 35.0<=x<=50.0:
	total=x+2.1
	print(round(total,2))
else:
	total=x+3.0
	print(round(total,2))