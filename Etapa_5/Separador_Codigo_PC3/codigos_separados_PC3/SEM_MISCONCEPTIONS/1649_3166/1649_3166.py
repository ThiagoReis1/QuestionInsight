from numpy import*
x = input("Digite a String: ").split(",")
y = zeros(5, dtype = int)
for v in range(size(x)):
	if (x[v] == "P"):
		y[0] = y[0] + 1
	elif(x[v] == "C")
	   y[1] = y[1] + 1
  	elif (x[v] == "M"):
		 y[2] = y[2] + 1
	elif (x[v] == "V"):
		 y[3] = y[3] + 1
	elif (x[v] == "A"):
		 y[4] = y[4] + 1
print(max(y))
print(y)		 
		 

