from numpy import*
v = array(input("").split(','))
f = zeros(5,dtype=int)
m = zeros(5,dtype=int)
for n in v:
		if(n == "P" ):
			f[0] = f[0] + 1 
			m[0] = m[0] + 1
		elif(n == "C"):
			f[1] = f[1] + 1
			m[1] = m[1] + 1
		elif(n == "R"):
			f[2] = f[2] + 1
			m[2] = m[2] + 1
		elif(n == "L"):
			f[3] = f[3] + 1
			m[3] = m[3] + 1
		elif(n == "B"):
			f[4] = f[4] + 1
			m[4] = m[4] + 1
print(max(m))
print(f)