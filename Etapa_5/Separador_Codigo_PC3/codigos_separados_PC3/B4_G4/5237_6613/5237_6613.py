a = int(input("n1: "))
b = int(input("n2: "))
c = int(input("n3: "))

x= a%2
y= b%2
z= c%2

if (x==0) and (y==0) and (z==0):
	print("SIM")
elif(x==0) and (y==0):
	print("SIM")
elif(y==0) and (z==0):
	print("SIM")
else:
	print("NAO")
	