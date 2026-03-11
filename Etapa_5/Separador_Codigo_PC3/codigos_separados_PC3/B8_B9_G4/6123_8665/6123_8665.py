c = float(input("combustivel"))

if (c < 17.5) :
	q = c+0.8
elif c>=17.5 and c<35:
	q = c+1.3
elif c>35 and c<50:
	q = c +2.1
elif c>= 50:
	q = c+3.0
print(q)