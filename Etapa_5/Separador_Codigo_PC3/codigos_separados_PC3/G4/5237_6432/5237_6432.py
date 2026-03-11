a = int(input(""))
b = int(input(""))
c = int(input(""))

ax = a % 2
bx = b % 2
cx = c % 2

if ((ax==0) and (bx==0)) or ((ax==0) and (cx==0)) or ((bx==0) and (cx==0)) or ((ax==0) and (bx==0) and (cx==0)):
	print("SIM")
else:
	print("NAO")
