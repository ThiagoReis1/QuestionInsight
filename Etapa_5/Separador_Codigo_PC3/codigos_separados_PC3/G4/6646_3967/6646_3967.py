from numpy import*
v = array(eval(input()))

vp = [1,2,3]
i = 0
mp = 0

while i < size(v):
	mp = mp + v[i] * vp[i]
	i = i + 1

mp = mp/sum(vp)
print(round(mp,2))