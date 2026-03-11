from numpy import*
a=array(eval(input('')))
i=0
pts= 0
while i < size(a):
	if a[i] == 1:
		pts += 100
	elif a[i] == 2:
		pts += 60
	elif a[i] == 3:
		pts += 20
	i += 1
	
print(round(pts,2))





