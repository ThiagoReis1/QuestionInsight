from numpy import*

cont = zeros(6,dtype=int)

cdp = input().upper().split(',')

mc = 0
c = 0
cm = 0
em = 0
e = 0
me = 0

for i in range(size(cdp)):
	if(cdp[i]=="MC"):
		mc = mc + 1
	elif(cdp[i]=="C"):
		c = c + 1
	elif(cdp[i]=="CM"):
		cm = cm + 1
	elif(cdp[i]=="EM"):
		em = em + 1
	elif(cdp[i]=="E"):
		e = e + 1
	elif(cdp[i]=="ME"):
		me = me + 1
		
cont[0] = mc
cont[1] = c
cont[2] = cm
cont[3] = em
cont[4] = e
cont[5] = me

print(max(cont))
print(cont)