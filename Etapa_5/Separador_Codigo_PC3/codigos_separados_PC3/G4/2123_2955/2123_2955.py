from numpy import*

# x=array([6.5,5.4,5.3,3.5])
x=array(eval(input()))
y=min(x)
s=x[0]+x[1]+x[2]+x[3]-y
media=s/3
if(media>=5):
	print(round(media,2))
	print("APROVOU")
else:
	print(round(media,2))
	print("REPROVOU")





