from numpy import*

x = array(eval(input("vetor: ")))

m = sum(x)/size(x)

d = 0
for n in range(size(x)):
	d = d + ((x[n]-m)**2)

d = (d/(size(x)-1))**0.5

print(round(d, 3))