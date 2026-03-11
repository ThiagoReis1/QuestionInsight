from math import*

x =float(input("Digite o valor de X: "))

if(x>2):
	v= x**(1/3)
	print(round(v,4))
elif(x>0) and (x<=1):
	print("1")
elif (x>1) and (x<=2):
	v = x**(1/2)
	print(round(v,4))
else:
	print("0")