dr= int(input("dias: "))

di = 175.00
tt = di*dr

t1 = tt+20.00
t2 = tt+16.00
t3 = tt+10.00
if dr < 15:
	print(round(t1, 2))
elif dr == 15:
	print(round(t2,2))
elif dr > 15:
	print(round(t3, 2))