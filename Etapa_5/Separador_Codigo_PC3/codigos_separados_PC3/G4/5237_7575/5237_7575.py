n1=int(input("n1: "))
n2=int(input("n2: "))
n3=int(input("n3: "))

a=n1%2
b=n2%2
c=n3%2

if((a!=0) and (b==0) and (c!=0) or (a==0) and (b!=0) and (c!=0) or (a!=0) and (b!=0) and (c==0)):
	print("NAO")
else:
	print("SIM")