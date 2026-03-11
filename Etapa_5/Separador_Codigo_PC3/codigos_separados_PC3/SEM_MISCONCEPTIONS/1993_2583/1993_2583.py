from math import * 

aminoacido = input()

if(aminoacido == cisteina):
	p = (12.011 * 3) + (1.00794 * 7) + (14.0067) + (15.9994 * 2) + 32.066
	print(p)
elif(aminoacido == isoleucina):
	p = (12.011 * 6) + (1.00794 * 13) + 14.0067 + (15.9994 * 2)
	print(p)
elif(aminoacido == metionina):
	p = (12.011 * 5) + (1.00794 * 11) + 14.0067 + (15.9994 * 2) + 32.066
	print(p)
else:
	print