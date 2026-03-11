combo = float(input())

x=combo*50

if combo>4:
	y= combo * 50- x*(12/100)
	print(round(y,2))
else:
	print(round(x,2))