from numpy import*

a = input("String: ").split(',')
b = 0
c = 0
d = 0
e = 0
f = 0
for i in range(len(a)):
	if(a[i] == "BE"):
		b = b + 1
		print(b)
	
	elif(a[i] == "ES"):
		c = c + 1
		print(c)
	
	elif(a[i] == "FR"):
		d = d + 1
		print(d)
	elif(a[i] == "IT"):
		e = e + 1
		print(e)
	elif(a[i] == "PT"):
		f = f + 1
		print(f)