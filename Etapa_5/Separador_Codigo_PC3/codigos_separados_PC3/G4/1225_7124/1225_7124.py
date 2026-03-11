from numpy import*
x= array(eval(input("")))
m= sum(x)/size(x)
cont= 0

for i in range(size(x)):
	cont= cont+ ((x[i]-m)**2)
c= (cont/(size(x)-1))**0.5

print (round(c,3))