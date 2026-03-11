am = 1.4
tm= 0.06
af = float(input())
tf = float(input())
y = 0
while(af>am):
	y +=1
	am += tm
	af += tf
print (y)
