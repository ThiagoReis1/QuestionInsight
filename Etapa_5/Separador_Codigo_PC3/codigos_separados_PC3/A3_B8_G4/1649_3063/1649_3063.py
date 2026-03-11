from numpy import*
v = input("digite o codigo: ")
v = v.split(',')
v0 = zeros(5,dtype= int)
s = 0
for i in range(size(v)):
	if(v[i]== "P"):
		v0[0]= v0[0] + 1
	elif(v[i]== "C"):
		v0[1]= v0[1] + 1
	elif(v[i]== "M"):
		v0[2]= v0[2] + 1
	elif(v[i]== "V"):
		v0[3]= v0[3] + 1
	elif(v[i]== "A"):
		v0[4]= v0[4] + 1
print(max(v0))
print((v0))