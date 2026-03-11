from numpy import*
s = input("").upper()
s = s.split(',')


vz = zeros(5, dtype = int)

for i in range(size(s)):
	if s[i] == "CHN":
		
		vz[0] += 1
	if s[i] == "JPN":
		
		vz[1] +=1
	if s[i] == "KOR":
		
		vz[2] +=1
	if s[i] == "MGL":
		
		vz[3] +=1
	if s[i] == "THA":
		
		vz[4] += 1

print(max(vz))
print(vz)



