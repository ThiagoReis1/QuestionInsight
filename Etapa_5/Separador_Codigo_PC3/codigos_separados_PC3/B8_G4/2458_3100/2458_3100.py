p = float(input())
c = int(input())
a1 = 0.1
a2 = 0.08
a3 = 0
a4 = 0.02
if(c == 1):
	t = p - (p * 0.40) + p * a1
	print(t)
elif(c == 2):
	t = p - (p * 0.40) + p * a2
	print(t)
elif(c == 3):
	t = p - (p * 0.40) + p * a3
	print(t)
elif(c == 4):
	t = p - (p * 0.40) + p * a4
	print(t)