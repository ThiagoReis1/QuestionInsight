from numpy import*
me=eval(input("nova cumpadi"))
mf=(sum(me)- min(me))/3
print(round(mf,2))
if mf>=5:
	print("APROVOU")
else:
	print("REPROVOU")