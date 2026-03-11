
a = input().upper()
i = 0
s = 0
while i < len(a):
	if a[i] == "B":
		s = s + 3.75
	elif a[i] == "C":
		s = s + 7.90
	elif a[i] == "E":
		s = s + 9.85
	i = i+1
print(round(s, 2))