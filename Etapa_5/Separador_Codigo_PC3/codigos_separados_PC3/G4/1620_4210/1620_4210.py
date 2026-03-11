from numpy import*
t = array(eval(input("tempo: ")))
p = array(eval(input("percentual: ")))/100

i = 0
while(i<size(t)):
	p[i] = p[i]*5
	i = i + 1

mult = t*p
print(round(sum(mult),2))
