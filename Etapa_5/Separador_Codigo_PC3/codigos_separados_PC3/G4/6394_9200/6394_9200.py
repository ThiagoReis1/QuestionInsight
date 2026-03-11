from numpy import*

a = array(eval(input("digite: ")))
			 
for i in range(size(a)):
	if(a[i] == 0 ):
		a[i] = 1
	elif(a[i] == 9):
		a[i] = 0
	else:
		a[i] -= -1 
print(a)