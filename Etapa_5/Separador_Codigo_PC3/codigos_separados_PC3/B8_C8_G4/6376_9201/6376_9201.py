from numpy import*

c = zeros(4,dtype=int)
b = input("digite").split(',')


for i in range(size(b)):
	if (b[i]=="A"):
		c[0] = c[0]+1
	elif(b[i] == "B"):
		c[1] = c[1] + 1
	elif(b[i] == "C"):
		c[2] = c[2] +1
	elif (b[i]=="D"):
		c[3] = c[3] +1
	i+=1	
print(c)
