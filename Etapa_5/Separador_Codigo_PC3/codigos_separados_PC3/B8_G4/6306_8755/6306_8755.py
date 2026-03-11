from numpy import * 
a = input("digite aqui: ")
i = 0 
d = 0
pa = 0
pl = 0
pp = 0

while d < len(a):
	if a[d] == "A":
		i = i + 19.90
		pa = pa + 1 
	elif a[d] == "L":
		i = i + 3.50
		pl = pl + 1
	elif a[d] == "P":
		i = i + 4.25
		pp = pp + 1
	d+=1
print(round(i,2), pa, pl, pp)
