cc = int(input())

if cc < 17.5:
	total = cc + 0.8
elif 17.5 < cc < 35:
	total = cc + 1.3
elif 35. < cc < 50:
	total = cc + 2.1
elif cc >= 50:
	total = cc + 3.

print(round(total, 1))