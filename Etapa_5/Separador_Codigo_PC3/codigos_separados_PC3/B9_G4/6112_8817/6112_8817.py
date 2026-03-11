com = int(input())

if com < 17.5:
	a = com + 10.5
	print(round(a,1))
elif com >= 17.5 and com < 35.0:
	a = com + 14.0
	print(round(a,1))
elif com	>= 35 and com < 50.0:
	a = com + 18.6
	print(round(a,1))
else:
	a = com + 24.5
	print(round(a,1))
		
