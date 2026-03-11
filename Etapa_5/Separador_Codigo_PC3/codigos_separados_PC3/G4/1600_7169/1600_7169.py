from numpy import* 
a = array(eval(input("digite: ")))
p = sum(a)
print(p)
i = 0
while i > len(a) :
	
	if a[i]>= 80:
		
		a[i] = a[i]-a[i]*15/100
		
	a[i] = a[i] + 1
print(round(sum(a),2))


