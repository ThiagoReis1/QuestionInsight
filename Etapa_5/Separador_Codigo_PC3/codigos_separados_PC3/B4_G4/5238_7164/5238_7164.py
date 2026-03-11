a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
if a<1000 and b<1000 and c<1000:
	print("NAO")
elif a>=1000 and (b<1000 and c<1000):
	print("NAO")
elif b>=1000 and (a<1000 and c<1000):
	print("NAO")
elif c>=1000 and (a<1000 and b<1000):
	print("NAO")
else:
	print("SIM")