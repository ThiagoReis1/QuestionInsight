x= float(input("x: "))

if(-100 <= x) and (x < 0):
	cal= (-1/x)
elif(x > 0) and (x <= 100):
	cal= 1/x
print(round(cal, 4))
if(x == 0):
	print('entrada invalida')