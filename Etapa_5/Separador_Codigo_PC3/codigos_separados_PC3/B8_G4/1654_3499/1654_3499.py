from numpy import*
s = input('siglas: ')
s = s.split(',')
p = zeros(5, dtype = int)
am = 0
pe = 0
sp = 0
rs = 0 
mg = 0
i = 0
for i in range(size(s)):
	if  s[i] == 'AM':
		am += 1
	elif s[i] == 'PE':
		pe += 1
	elif s[i] == 'MG':
		mg += 1
	elif s[i] == 'SP':
		sp += 1
	elif s[i] == 'RS':
		rs += 1
p[0] = am
p[1] = pe
p[2] = mg
p[3] = sp
p[4] = rs
print(max(p))
print(p)