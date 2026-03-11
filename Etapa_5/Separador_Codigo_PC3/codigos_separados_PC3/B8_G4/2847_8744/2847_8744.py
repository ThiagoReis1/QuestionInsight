from numpy import*

d = array(eval(input("digite o codigo: ")))
 
for i in range(size(d)):
	if(d[i] == 0):
		d[i] = 0 ** 2
	elif(d[i] == 1):
		d[i] = 1 ** 2
	elif(d[i] == 2):
		d[i] = 2 ** 2
	elif(d[i] == 3):
		d[i] = 3 ** 2
	elif(d[i] == 4):
		d[i] = 4 ** 2
	elif(d[i] == 5):
		d[i] = 5 ** 2
	elif(d[i] == 6):
		d[i] = 6 ** 2
	elif(d[i] == 7):
		d[i] = 7 ** 2
	elif(d[i] == 8):
		d[i] = 8 ** 2
	elif(d[i] == 9):
		d[i] = 9 ** 2

print(d)