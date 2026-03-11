from numpy import*

v=array(eval(input()))

mf=sum(v)- min(v)

mt= mf / 3
	
if(mt>=5):
	print(round(mt,2))
	print("APROVOU")
else:
	print(round(mt,2))
	print("REPROVOU")
  