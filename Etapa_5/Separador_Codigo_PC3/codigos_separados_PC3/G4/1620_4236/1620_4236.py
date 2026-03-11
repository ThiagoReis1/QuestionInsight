from numpy import*
t = array(eval(input("tempo: ")))
p = array(eval(input("percentual: ")))

tam = size(t)
total = 0
i = 0

while i < tam:
	total = total + t[i]*5*p[i]/100
	i = i + 1
print(round(total, 2))