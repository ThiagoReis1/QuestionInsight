comum = float(input())

if(comum <= 17.5):
	mis = comum+10.5
elif(comum<35.0):
	mis = comum+14.0
elif(comum<50.0):
	mis = comum+18.6
else:
	mis = comum+24.5
	
print(round(mis, 2))