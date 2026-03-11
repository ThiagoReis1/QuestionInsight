x = input("Isoleucina ou Metionina: ").lower()
o = 15.9994
c = 12.011
n = 14.0067
s = 32.066
h = 1.00794

if(x == "isoleucina"):
	a = c*6+h*13+n+o*2
	print(round(a,2))
else:
	b = c*5+h*11+n+o*2+s
	print(round(b, 2))