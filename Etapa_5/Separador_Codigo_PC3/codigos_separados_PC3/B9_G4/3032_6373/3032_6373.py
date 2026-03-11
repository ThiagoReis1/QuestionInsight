x = float(input("digite o valor de x:"))
if(x<=0):
	f= 0 
elif (x > 0 and x <=1):
	f =1
elif (x > 1 and x  <= 2):
	f = x**(1/2)
else:
	f = x**(1/3)
print(abs(round(f, 4)))