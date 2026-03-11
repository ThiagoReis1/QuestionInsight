ppp = float(input("peso por pacote: "))

if ppp < 5:
	t = (ppp*10 + ppp*003.75)
elif ppp == 5:
	t = (ppp*10 + ppp*004.75)
elif ppp > 5: 
	t = (ppp*10 + ppp*005.75)
print(round(t,4))
	