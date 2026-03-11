from numpy import*

v= array(eval(input("Vetor: ")))

ct= sum(v)
d=0

if(size(v) <= 80):
	d=d 
else:
	d= 5/100
	ct= ct * d
print(round(ct, 2))