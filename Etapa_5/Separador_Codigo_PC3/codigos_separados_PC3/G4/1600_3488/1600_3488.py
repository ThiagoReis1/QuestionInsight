from numpy import*

a = array(eval(input("valor da compra: ")))
i = 0
desc = (15/100)

c = 0
d = 0


while(i < size(a)):
	if(a[i] > 80):
		c = a[i] - a[i] * desc + c
	else:
		d = d + a[i]
	i = i + 1

print(round(sum(c)+sum(d), 2))