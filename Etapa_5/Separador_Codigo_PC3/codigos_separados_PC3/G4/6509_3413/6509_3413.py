def hph(h,n):
	total = 28.50 * n
	if h >= 18:
		des = total * 0.20
		total -= des
		
	print(round(total,2))
	
hph(int(input()),int(input()))