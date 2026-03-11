alf = float(input(""))
tf = float(input(""))
alm = 1.86
tm = 0.01
c = 0
while alf <= alm:
	alm = alm + tm
	alf = alf + tf
	c = c+1
print(c)
	