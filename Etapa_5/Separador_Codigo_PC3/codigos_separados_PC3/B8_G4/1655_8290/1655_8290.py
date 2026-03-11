from numpy import *

e = input('Estados: ').upper().split(',')
v = ones (5, dtype=int)
vn = [1,2,3,4,5]
ac = 0
am = 0
pa = 0
ro = 0
rr = 0

for i in e: 
	if (i == 'AC'):
		ac = ac + 1
	elif (i == 'AM'):
		am = am + 1
	elif (i == 'PA'):
		pa = pa + 1
	elif (i == 'RO'):
		ro = ro + 1
	elif (i == 'RR'):
		rr = rr + 1
		
for o in vn:
	if (o == 0):
		v[o] = ac
	elif (o == 1):
		v[o] = am
	elif (o == 2):
		v[o] = pa
	elif (o == 3):
		v[o] = ro
	elif (o == 4):
		v[o] = rr
		
print(max(v))
print(v)
