from numpy import*

x1 = array(eval(input("Entrada: ")))

c1=0
d1= 0

for i in range(size(x1)):
	if x1[i] <= 50:
		c1 = c1+1
		

		
b1 = zeros(c1,dtype=int)

for i in range(size(x1)):
	if x1[i] <= 50:
		b1[d1] = i
		
		d1 = d1+1

print(c1)
		
print(b1)
		
	

	