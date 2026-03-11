s = input('determine a secao: ').upper()

i = 0
t = round(0, 2)

while i < len(s):
	if s[i] == 'M':
		t = t + 7.25
	elif s[i] == 'P':
		t = t + 4.75
	elif s[i] == 'R':
		t = t + 3.50
	i = i + 1
print(t)