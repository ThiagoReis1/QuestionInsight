from numpy import*
a = input("países:").split(',')
p = array(["AZ","CA","FL","PA","WI"])
b = array([0,0,0,0,0])

c = 0
for i in (a):
	if(i==p[0]):
		b[0] += 1
	elif(i==p[1]):
		b[1] += 1
	elif(i==p[2]):
		b[2] += 1
	elif(i==p[3]):
		b[3] += 1
	elif(i==p[4]):
		b[4] += 1
print(max(b))
print(b)
		