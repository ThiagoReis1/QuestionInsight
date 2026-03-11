from numpy import*
s = input("").split(',')
az = 0
ca = 0
fl = 0
pa = 0
wi = 0
d = zeros(5,dtype = int)
for a in range(size(s)):
		if(s[a] == "AZ"):
			az = az + 1
			d[0] = az
		if(s[a] == "CA"):
			ca= ca + 1
			d[1] = ca
		if(s[a] == "FL"):
			fl = fl + 1
			d[2] = fl
		if(s[a] == "PA"):
			pa = pa + 1
			d[3] = pa
		if(s[a] == "WI"):
			wi = wi + 1
			d[4] = wi
m = print(max(d))
print(d)

		