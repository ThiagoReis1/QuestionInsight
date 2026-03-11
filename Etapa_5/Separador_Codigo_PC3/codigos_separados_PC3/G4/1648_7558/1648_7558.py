from numpy import*

p = array(eval(input()))
a = 0
b = ""
for i in range(size(p)):
	if(p[i] < 70):
		a+=1
		b = b + str(i)+","
print(a)
print(array(eval(b)))