from numpy import*
x = str(input()).split(",")
i = 0
a = 0
p = 0
r = 0
m = 0
s = 0
while (size(x)>i):
	if(x[i]=="AM"):
		a = a + 1
	elif(x[i]=="PE"):
		p = p + 1
	elif(x[i]=="RS"):
		r = r + 1
	elif(x[i]=="MG"):
		m = m + 1
	elif(x[i]=="SP"):
		s = s + 1
	i = i + 1
print(max(a,p,r,m,s))
y = array([a,p,m,s,r])
print(y)
