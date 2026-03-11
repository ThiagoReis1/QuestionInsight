a = int(input("Leia a: "))
b = int(input("Leia b: "))
c = int(input("Leia c: "))

if (a//2) and (b//2) and (c//2):
	print("SIM")
elif(a//2) or (b//2) or (c//2):
	print("SIM")
elif (a//2) and (b//2) or (c//2):
	print("SIM")
elif (a//2) or (b//2) and (c//2):
	print("SIM")
elif (a//2) or (c//2) and (b//2):
	print("SIM")
else:
	print("NAO")
	
