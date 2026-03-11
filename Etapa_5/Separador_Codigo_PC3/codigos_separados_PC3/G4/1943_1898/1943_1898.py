am = input("digite nome do aminoacido: ")

o = 15.9994
c = 12.011
n = 14.0067
e = 32.066
h = 1.00794

iso = ((c*6)+(h*13)+(n)+(o* 2))
met = ((c*5)+(h*11)+(n)+(o*2)+e)

if	(am.lower() == "isoleucina"):
		print(round(iso , 2))
else:
		print(round(met , 2))
