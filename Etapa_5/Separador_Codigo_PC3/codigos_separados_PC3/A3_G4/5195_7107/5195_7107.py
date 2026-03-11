dc = float(input())
tc = float(input())

dc = (dc * 1000)

pc = 30 * (dc / 10)


if(pc > dc):
	
	print(round(pc, 2))
	print("vai conseguir")
	
else:
	
	print(round(pc, 2))
	print("nao vai conseguir")