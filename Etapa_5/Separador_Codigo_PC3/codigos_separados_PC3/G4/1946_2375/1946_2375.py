nome = str(input())
nom= nome.lower()

o=15.9994
c=12.011
n=14.0067
s=32.066
h=1.0079

if(nom == "fenilalanina"):
	peso= c*9+h*11+o*2+s
	
else:
	peso= c*9+h*11+n+o*3
	
p=round(peso,2)
print(p)