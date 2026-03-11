from numpy import*

t = array(eval(input("tempo dos banhos: ")))
m = array(eval(input("modos dos banhos: ")))

if(size(m) == "QUENTE"):
	m = 90
elif(size(m)=="MORNO"):
	m = 45
else:
	m = 0
	
i = 0
ct = 0
while(i < size(t)):
	i = i + 0 
	ct = m[i] * t[i] * 0.005
print(ct)
	
	

		
		
	

	

	
	

