from numpy import*

a = array(eval(input("digite:")))
k = [0,1,2,3,4,5,6,7,8,9]


for i in range(size(a)):
	if(a[i] == k[0]):
		a[i] = 1
	elif (a[i] == k[1]):
		a[i] = 2**3
	elif(a[i] == k[2]):
		a[i] = 3**3
	elif (a[i] == k[3]):
		a[i] = 4**3
	elif (a[i] ==k[4]):
		a[i] = 5**3
	elif(a[i]== k[5]):
		a[i] = 6**3
	elif(a[i]== k[6]):
		a[i]= 7**3
	elif(a[i]== k[7]):
		a[i] = 8**3
	elif(a[i] == k[8]):
		a[i] = 9**3
	elif(a[i]== k[9]):
		a[i] = 0
	i+=1
print(a)