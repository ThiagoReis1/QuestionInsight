nbi=float(input())
tc=float(input())/100
nba=nbi
nbf=nbi*2
h=0

while nba<nbf:
	nba+=nba*tc
	h+=1
print(h)