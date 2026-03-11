from numpy import*

entr = input("quantas frutas em iniciais: ")
i = 0
pre = 0

h = 0
l = 0
e = 0

while i < len(entr):
	if entr[i] == "H":
		pre = pre + 3.85
		h = h+1
	elif entr[i] == "L":
		pre = pre + 2.95
		l = l + 1
	elif entr[i] == "E":
		pre = pre + 7.90
		e = e + 1
	i = i + 1
preco = round(pre,2)

print(preco,h,l,e)