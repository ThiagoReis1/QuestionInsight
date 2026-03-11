a = float(input(":"))
seconds = 0

while(a>=40) :
	a = a - (a*0.02)
	seconds= seconds + 1
	
print(seconds)