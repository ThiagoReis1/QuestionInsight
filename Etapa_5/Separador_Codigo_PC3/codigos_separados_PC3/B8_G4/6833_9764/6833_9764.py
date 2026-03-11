from numpy import*
n = input("reais: ").upper()
i = 0
s = 0
tan = len(n)
#produtos:
M = 7.25
P = 4.75
R = 3.50
while i < tan:
	if n[i] == 'M':
		s = s + M
	if n[i] == 'P':
		s = s + P
	elif n [i] == 'R':
		s = s + R
	i = i + 1
print(round(s,2))
