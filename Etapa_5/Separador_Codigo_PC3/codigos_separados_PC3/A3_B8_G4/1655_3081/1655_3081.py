from numpy import*
x = input("Estados: ")
y = x.split(',')
AM = 0
AC = 0
PA = 0
RO = 0
RR = 0
est = 0
est2 = 0
est3 = 0
est4 = 0
est5 = 0
for i in y:
	if(i=="AM"):
		AM = AM + 1
	elif(i=="AC"):
		AC = AC + 1
	elif(i=="PA"):
		PA = PA + 1
	elif(i=="RO"):
		RO = RO + 1
	elif(i=="RR"):
		RR = RR + 1
if(AM>0):
	est = 1
if(AC>0):
	est2 = 1
if(PA>0):
	est3 = 1
if(RO>0):
	est4 = 1
if(RR>0):
	est5 = 1
j = zeros(5,dtype=int)
j[0] = AC
j[1] = AM
j[2] = PA
j[3] = RO
j[4] = RR
print(max(j))
print(j)
	
