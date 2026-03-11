n = int(input("pizza: "))

if n == 3 :
	t = 3.25
else:
	if n < 3:
		t = 3.00
	else:
		t = 4.50
		
c = 5*n + t

print(round(c, 2))