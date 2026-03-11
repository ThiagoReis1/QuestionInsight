m = input().upper()
CARA = 0
COROA = 0
while m !="S":
		CARA = CARA + 1
		COROA = COROA + 1
		H = COROA + CARA
		m = input().upper()
		if m == "S":
			print(H)
			pa = (CARA*100)/H
			print(round(pa,2))
			
		
		
		
	
	
