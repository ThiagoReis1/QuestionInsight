from numpy import*

a = input("estados: ").split(",")
i = 0
ac = 0
am = 0 
pa = 0 
ro = 0 
rr = 0


while i < len(a):
	if (a[i] == "AC"):
		ac = ac + 1
		i = i + 1
	elif (a[i] == "AM"):
		am = am + 1
		i = i + 1
	elif (a[i] == "PA"):
		pa = pa + 1
		i = i + 1
	elif (a[i] == "RO"):
		ro = ro + 1
		i = i + 1
	elif (a[i] == "RR"):
		rr = rr + 1
		i = i + 1
	
b = array([ac,am,pa,ro,rr])

print(max(b))
print(b)
		
		