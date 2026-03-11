from numpy import*

vp = array(eval(input("Digite os andares que parou: ")))


i = 1
d = 0
total = 0

while(i<size(vp)):
	d = vp[i]-vp[i-1]
	total = total + d
	i = i + 1

print(total)







