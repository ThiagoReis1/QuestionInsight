from numpy import*
a = input("sigla: ").split(",")
k = 0
ac = 0
am = 0
pa = 0
ro = 0
rr = 0
for i in a:
	if (i.upper()=="AC"):
		ac = ac + 1
	elif (i.upper()=="AM"):
		am = am + 1
	elif (i.upper()=="PA"):
		pa = pa + 1
	elif (i.upper()=="RO"):
		ro = ro + 1
	elif (i.upper()=="RR"):
		rr = rr + 1
b = zeros(5, dtype=int)
for n in b:
	if(k==0):
		b[k] = ac
	elif(k==1):
		b[k] = am
	elif(k==2):
		b[k] = pa
	elif (k==3):
		b[k] = ro
	elif (k==4):
		b[k] = rr
	k = k + 1
print(max(b))
print(b)