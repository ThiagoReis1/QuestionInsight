x = float(input())

if x <= -1 or x >=1:
	f = x ** 2 
elif (x > -1 and x < 0) or (x > 0 and x < 1):
	f = x
else:
	f = 1
	
print(round(f,4 ))