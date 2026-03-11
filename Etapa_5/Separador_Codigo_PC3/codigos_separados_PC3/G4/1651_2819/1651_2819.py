from numpy import *
vs = input("")
v = vs.split(',')
s = zeros(6, dtype=int)
mc = 0
c = 0
cm = 0
em = 0
e = 0
me = 0
for x in v:
	if(x.upper() == "MC"):
		mc += 1
	elif(x.upper() == "C"):
		c+= 1
	elif(x.upper() == "CM"):
		cm+= 1
	elif(x.upper() == "EM"):
		em+= 1
	elif(x.upper() == "E"):
		e+= 1
	else:
		me += 1
print(max(mc, c, cm, em, e, me))
s[0] = mc
s[1] = c
s[2] = cm
s[3] = em
s[4] = e
s[5] = me
print(s)