x = float(input())
k = int(input())

r=1
#tg
#exp = 2*r-1
#den = exp
arcx = 0
while(r<=k):
	arcx = arcx+(x**(2*r-1))/(2*r-1)
	r = r+1
print(round(arcx,7))