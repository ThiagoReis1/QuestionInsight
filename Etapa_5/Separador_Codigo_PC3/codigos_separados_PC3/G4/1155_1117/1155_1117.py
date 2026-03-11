v=int(input())
l=int(input())
tv=float(input())
tl=float(input())
d=0
while l!=2*v:
	v=v+ v*tv
	l=l+ l*tl
	d=d+1
print(d)
	