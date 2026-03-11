from numpy import*

v= array(eval(input()))



im=0
t=0

for i in range(size(v)):
   if(v[i]%2!=0):
      im=im+1
y= zeros(im, dtype= int)
for x in range(size(v)):
	if(v[x]%2!=0):
		y[t]= v[x]
		t= t + 1
				
print(y)