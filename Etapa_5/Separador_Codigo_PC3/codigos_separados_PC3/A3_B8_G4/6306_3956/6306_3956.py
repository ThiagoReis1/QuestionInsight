ac = 19.9
lat = 3.5
pad = 4.25

entrada = input()
a=0
aq = 0
l=0
lq = 0
p=0
pq = 0
for i in range(len(entrada)):
	if entrada[i]=='A':
		a = a + 19.9
		aq = aq+1
	elif entrada[i]=='L':
		l = l + 3.5
		lq = lq+1
	elif entrada[i]=='P':
		p = p + 4.25
		pq=pq+1
		
print(round(a+l+p, 2), aq, lq, pq)
