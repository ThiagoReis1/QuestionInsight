n1 = int(input("num 1: "))
n2 = int(input("num2:  "))
n3 = int(input("num3:  "))

if (n1%2==0) and (n2 %2 == 0):
	print("SIM")
elif (n3 %2 == 0) and (n1 %2 == 0):
	print("SIM")
elif (n2 %2 ==0) and (n3 %2 ==0):
	print("SIM")
else:
	print("NAO")