nome= input().lower()

o=15.9994
c=12.011
n=14.0067
s=32.066
h=1.0079

if(nome=="fenilalanina"):
	t= (c*9) + (h * 11) + (o*2) + s
	print(round(t,2))
else:
	p= (c*9) + (h*11) + (n) + (o*3)
	print(round(p,2))
	