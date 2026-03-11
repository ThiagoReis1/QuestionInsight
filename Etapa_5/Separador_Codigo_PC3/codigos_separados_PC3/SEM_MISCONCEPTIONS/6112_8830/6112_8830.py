ct = float(input("quanto voce tem de combustivel?: "))

if ct <= 17.5:
	qt_add = 10.5
	mistura = ct + qt_add
	print(round(mistura,1))
	
elif ct >= 17.5 and ct < 35.0:
	qt_add = 14.0
	mistura = ct + qt_add
	print(round(mistura,1))
	
elif ct >= 50:
	qt_add = 24.5
	mistura = ct + qt_add
	print(round(mistura,1))
	
else:
	qt_add = 18.6
	mistura = ct + qt_add
	print(round(mistura,1))
	