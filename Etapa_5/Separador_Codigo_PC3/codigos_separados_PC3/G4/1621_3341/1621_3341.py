from numpy import*
a = array(eval(input("valores: ")))
b = array(eval(input("valores: ")))
a[0] = 1.25
a[1] = 2.60
a[2] = 1.80
a[3] = 0.85
a[4] = 3.20
i = 0
total = 0
while(i<5):
	total = total + a[i]*b[i]
	i = i + 1
print(round(total, 2))	