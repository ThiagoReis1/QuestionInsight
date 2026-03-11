from numpy import*
v=array(eval(input()))
mi=min(v)
s=sum(v)-mi
med=round(s/3,2)
print(med)
if(med>=5):
	print("APROVOU")
else:
	print("REPROVOU")
	