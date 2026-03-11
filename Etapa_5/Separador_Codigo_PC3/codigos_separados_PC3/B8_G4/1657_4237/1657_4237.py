from numpy import*
x = input("estados: ").split(',')

ca = zeros(5, dtype)

for i in x:
	if(i == "AZ"):
		ca[0]= ca[0] + 1
	elif(i=="CA"):
		ca[1] = ca[1] + 1
	elif(i=="FL"):
		ca[2] = ca[2] + 1
	elif(i=="PA"):
		ca[3] = ca[3] + 1
	elif(i=="WI"):
		ca[4] = ca[4] + 1

print(max(ca))
print(ca)
		

