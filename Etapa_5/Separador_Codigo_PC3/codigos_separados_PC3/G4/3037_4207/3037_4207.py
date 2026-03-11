x= float(input("Digite um valor para X: "))

if(x<=-1 or x>=1):
	fx= x**2
	print(round(fx, 4))
elif((x<-1 and x<0) or (x>0 and x<1)):
	fx= x
	print(round(fx, 4))
else:
	fx= 1
	print(round(fx, 4))