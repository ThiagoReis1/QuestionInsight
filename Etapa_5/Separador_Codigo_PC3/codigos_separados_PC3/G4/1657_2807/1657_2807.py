from numpy import*

y = zeros(5, dtype=int)
x = input("").split(",")

for i in range(size(x)):
	if(x[i] == "AZ"):
		y[0] += 1
	elif(x[i] == "CA"):
		y[1] += 1
	elif(x[i] == "FL"):
		y[2] += 1
	elif(x[i] == "PA"):
		y[3] += 1
	else:
		y[4] += 1

print(max(y))
print(y)