m = float(input('qual a massa de sua encomenda (em quilogramas)? '))
if m < 5000.0 :
	fr = 0.05 * m
	print("%.2f" % fr)
else:
	fr = 60 + 0.04 * m
	print('%.2f' % fr)