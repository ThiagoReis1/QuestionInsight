from numpy import*
s = input().split(",")
v = zeros(5, dtype= int)
for x in range(size(s)):
	if s[x] == "AR":
		v[0] = v[0] + 1
	elif s[x] == "BR":
		v[1] = v[1] + 1
	elif s[x] == "CL":
		v[2] = v[2] + 1
	elif s[x] == "CO":
		v[3] = v[3] + 1
	elif s[x] == "UY":
		v[4] = v[4] + 1
print(max(v))
print(v)