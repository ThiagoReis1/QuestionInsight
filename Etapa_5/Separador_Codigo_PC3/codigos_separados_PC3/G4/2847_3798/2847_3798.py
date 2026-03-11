from numpy import*
v=array(eval(input("codigo ")))
for i in range(size(v)):
	if(v[i]>=0 and v[i]<=9):
		cf=v**2
print(cf)