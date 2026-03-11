bs = input('bolo ou slagado:')
qnts = int(input('quantos?'))
cafe = int(input('qnts cafe:'))

if bs.upper() == 'B':
	b = (5 * qnts) + (cafe * 7.5)
	print(round(b,2))
	
if bs.upper() == 'S':
	h = (4 * qnts) + (cafe * 7.5)
	print(round(h,2))