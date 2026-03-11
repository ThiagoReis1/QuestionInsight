pt = int(input())
pp = int(input())
cpt = float(input())
cpp = float(input())
nmax = int(input())
anos = 1
while(nmax >= (pt + pp)):
	pt = pt*(1 + cpt)
	pp = pp*(1 + cpp)
	anos = anos + 1
print(anos)
