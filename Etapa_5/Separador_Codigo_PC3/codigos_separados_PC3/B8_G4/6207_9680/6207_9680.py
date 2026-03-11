x1 = int(input())

tt = 0 

while x1 != -1:
	if x1 >= 26 and x1 <= 50:
		tt = tt + 1
		x1 = int(input())
	elif x1 == -1 :
		print(tt)
		break