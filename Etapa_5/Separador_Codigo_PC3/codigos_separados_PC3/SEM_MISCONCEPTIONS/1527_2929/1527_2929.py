
t = 0

acumF= int(input())
acumL= int(input())
cent1 = float(input())
cent2 = float(input())

while(acumL<= acumF ):
	
	acumF = acumF + (acumF* (cent1/100))
	acumL= acumL+ (acumL* (cent2/100))
	t= t+1
	
print(t)
