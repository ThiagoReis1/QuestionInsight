fuel = float(input())

if(fuel < 17.5):
	Li2 = 10.5
elif(fuel < 35.0):
	Li2 = 14.0
elif(fuel < 50.0):
	Li2 = 18.6
else:
	Li2 = 24.5
	
total = fuel + Li2
print(round(total, 1))