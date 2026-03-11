n1= int(input())
n2= int(input())
n3= int(input())
if (n1%2)==0 and (n2%2)==0 and not (n3%2)==0:
	print("SIM")
elif (n3%2)==0 and (n2%2)==0 and not (n1%2)==0:
	print("SIM")
elif (n1%2)==0 and (n2%2)==0 and (n3%2)==0:
	print("SIM")
else:
	print("NAO")