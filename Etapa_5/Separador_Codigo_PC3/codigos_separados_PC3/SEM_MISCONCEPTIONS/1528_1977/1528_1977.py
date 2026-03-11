qt_g = int(input())
qt_troll = int(input())
qt_rec = int(input())
r = 0
while qt_troll > 0:
	qt_troll = (qt_troll -5*qt_g) + qt_rec
	r = r + 1
print(r)	