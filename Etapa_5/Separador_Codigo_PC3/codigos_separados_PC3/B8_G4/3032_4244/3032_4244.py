x = float(input())

if(0>=x):
	y = 0
elif(1>=x>0):
	y = 1
elif(2>=x>1):
	y = x**(1/2)
elif(x>2):
	y = x**(1/3)
print(round(y, 4))
	