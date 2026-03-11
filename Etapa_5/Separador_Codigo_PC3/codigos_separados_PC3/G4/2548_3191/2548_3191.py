s = str(input('Digite uma str: ')).upper()
s = s + ' '
r = ''
i = 0
j = 0
k = 0
while i < len (s):
	if s[i] == ' ':
		t = s[j:i]
		r = r + t[k]
		k += 1
		j = i 
	i+= 1
print(r)