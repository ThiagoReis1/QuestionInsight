m = input().lower()

o= 15.9994
c = 12.011
n = 14.0067
s = 32.066
h = 1.00794

if (m == "aspartato") or (m == "cisteina") or (m == "metionina"):
	if m == "aspartato":
		p = ((c*4) + (h*6) + (n) + (o*4))
	elif m == "cisteina":
		p = ((c*3) + (h*7) + (n) + (o*2) + (s))
	elif m == "metionina":
		p = ((c*5) + (h*11) + (n) + (o*2) + (s))
	print(round(p, 2))
else:
	print("Dado Invalido")