from numpy import*
s = input().split(',')
i = 0 
ac = 0 
am = 0 
pa = 0 
ro = 0 
rr = 0
z = zeros(5, dtype=int)
while(i<len(s)):
	if(s[i] == "AC"):
		ac = ac + 1
		z[0] = z[0] + 1
	if(s[i] == "AM"):
		am = am + 1	
		z[1] = z[1] + 1
	if(s[i] == "PA"):
		pa = pa + 1
		z[2] = z[2] + 1
	if(s[i] == "RO"):
		ro = ro + 1
		z[3] = z[3] + 1
	if(s[i] == "RR"):
		rr = rr + 1
		z[4] = z[4] + 1
	i = i + 1 
print(max(ac,am,pa,ro,rr))	
print(z)


	