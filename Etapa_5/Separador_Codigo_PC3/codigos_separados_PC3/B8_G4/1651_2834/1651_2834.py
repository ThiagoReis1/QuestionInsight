from numpy import *

t = input("tons: ").upper().split(',')

mc = 0
c = 0
cm = 0
em = 0
e = 0
me = 0

cont = zeros(6, dtype = int)

for i in range(len(t)):
	if(t[i] == "MC"):
		mc = mc + 1
		cont[0] = mc
	elif(t[i] == "C"):
		c = c + 1
		cont[1] = c
	elif(t[i] == "CM"):
		cm = cm + 1
		cont[2] = cm
	elif(t[i] == "EM"):
		em = em + 1
		cont[3] = em
	elif(t[i] == "E"):
		e = e + 1
		cont[4] = e
	elif(t[i] == "ME"):
		me = me + 1
		cont[5] = me	

print(max(cont))
print(cont)