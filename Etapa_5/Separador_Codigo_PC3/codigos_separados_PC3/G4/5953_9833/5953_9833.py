L = input() 
P = int(input())
R = int(input()) 

if L == "L":
	total = P * 6 + R * 3 
	print(round(total, 2))
	
else: 
	total = P * 13.50 + R * 3
	print(round(total, 2))
	