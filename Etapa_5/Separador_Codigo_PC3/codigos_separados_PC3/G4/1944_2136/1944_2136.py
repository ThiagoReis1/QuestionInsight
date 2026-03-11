amn = input("leucina ou lisina? ").lower()

o = 15.9994
c = 12.011
n = 14.00674
h = 1.0079

if(amn == "leucina"):
	pm = 6*c + 13*h + n +2*o

else:
	pm = 6*c + 15*h + 2*n + 2*o
	
print(round(pm,2))