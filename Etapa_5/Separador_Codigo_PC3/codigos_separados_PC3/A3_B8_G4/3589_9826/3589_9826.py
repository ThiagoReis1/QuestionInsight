from numpy import*

vn = array(eval(input("digite:")))
pt = 0
an = array([1, 2, 3, 4])
i = 0
while  i < len(vn):
	an = vn[i]
	if an == 1:
		pt +=80
	elif an == 2:
		pt +=40
	elif an == 3:
		pt +=20
	elif an == 4:
		pt +=10	   
	i += 1
print(round(pt, 2 ))