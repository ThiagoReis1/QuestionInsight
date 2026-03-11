status = input("(T) para tapioca e (S) para salgado:")

qt1= int(input("digite:"))
qt2 = int(input("digite:"))
T= 4.5
S= 5.00
A =12.00

if status == "T":
	total= qt1*T+qt2*12
	
else:
	var1 = qt1*S
	total = var1+(qt2*12)
	
print(round(total, 1))