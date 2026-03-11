nome_do_aminoacido=input("digiteo nome:(glutamina/treonina)")
o=15.9994
c=12.011
n=14.0067
h=1.00794
if(nome_do_aminoacido.upper()=="GLUTAMINA"):
	pm=c*5+h*8+n*1+o*4
	print(round(pm,2))
else:
	pm=c*4+h*9+n+o*3
	print(round(pm,2))