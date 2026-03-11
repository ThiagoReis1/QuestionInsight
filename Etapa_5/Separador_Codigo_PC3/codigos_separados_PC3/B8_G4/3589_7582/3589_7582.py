from numpy import*
v = array(eval(input("anel ")))
p = 0
for a in v:
	if a == 1 :
		p += 80
	elif a == 2:
		p += 40
	elif a == 3 :
		p += 20
	elif a == 4:
		p += 10
print(p)