from numpy import*
nota= array(eval(input("")))
soma = nota[0] + nota[1] + nota[2] + nota[3]
mf=((soma)- min(nota))/3

print(round(mf, 2))

if(mf>= 5):
	print("APROVOU")
else:
	print("REPROVOU")
