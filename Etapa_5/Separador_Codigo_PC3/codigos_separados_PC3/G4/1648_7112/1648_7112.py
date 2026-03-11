from numpy import*

a = array(eval(input("notas: ")))

x = 0
rf = 0

for i in range(size(a)):
	if(a[i] < 70):
		rf = rf +1 
		
v = zeros(rf, dtype = int)
for i in range(size(a)):
	if( a[i]< 70):
		v[x]= i
		x = x+1
	
print(rf)
print(v)