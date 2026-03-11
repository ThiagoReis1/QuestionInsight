from numpy import*
s = input('siglas: ')
s = s.split(',')
p = zeros(5, dtype = int)
ar = 0
br = 0
cl = 0
co = 0 
uy = 0
i = 0
for i in range(size(s)):
	if  s[i] == 'AR':
		ar += 1
	elif s[i] == 'BR':
		br += 1
	elif s[i] == 'CL':
		cl += 1
	elif s[i] == 'CO':
		co += 1
	elif s[i] == 'UY':
		uy += 1
p[0] = ar
p[1] = br
p[2] = cl
p[3] = co
p[4] = uy
print(max(p))
print(p)



		
			  


