x=input("qual peso molecular:").lower()#isoleucina ou Metionina
o=15.9994
c=12.011
n=14.0067
s=32.066
h=1.00794
if(x=='isoleucina'):
	f=((6*c)+(h*13)+n+(o*2))
	print(round(f,2))
else:
	g=(c*5)+(h*11)+n+(o*2)+s
	print(round(g,2))







