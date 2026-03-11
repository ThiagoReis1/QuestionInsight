from numpy import*

n= array(eval(input()))

sum(n)
size(n)
max(n)

v= sum(n) - max(n)
mf= v/3

if(mf >= 5):
	print(round(mf,2))
	print("APROVOU")
else:
	print(round(mf,2))
	print("REPROVOU")


