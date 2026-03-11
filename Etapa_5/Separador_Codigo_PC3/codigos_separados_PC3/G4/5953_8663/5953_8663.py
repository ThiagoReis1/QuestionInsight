lp = input()
q = int(input())
r = int(input())

pl = 6*q + 3*r
pp = 13.5*q + 3*r

if lp.upper() == "L":
	v = pl
else:
	v = pp
print(round(v, 2))