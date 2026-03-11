from numpy import*

notas= array(eval(input()))

me= ((sum(notas))-(min(notas)))/3
print(round(me,2))

if me >= 5:
	print("APROVOU")
else:
	print("REPROVOU")
				 