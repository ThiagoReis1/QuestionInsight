x = float(input())
k = int(input())

pt = 1
ct = 0
arc = 0

while(ct < k):
	arc = arc + (x**(pt)/(pt))
	pt = pt + 2
	ct = ct + 1

print(round(arc, 7))