pts = 100
acertos = eval(input())

i = 0
while i < len(acertos):
	if acertos[i] == 1:
		pts = pts * 5
	elif acertos[i] == 2:
		pts = pts * 3
	elif acertos[i] == 3:
		pts = pts
	else:
		pts = pts / 2.0
	i += 1
print(round(pts, 2))