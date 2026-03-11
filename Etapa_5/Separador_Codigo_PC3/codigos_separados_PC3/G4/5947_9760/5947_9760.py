A = input("C ou E:")
q = int(input("quantidade de coxinhas ou esfirras: "))
s= int(input("quantidade de suco: "))

if A =="C":
	t = q*2 + s*6
	print(round(t, 1))
else:
	t = q*4.5 + s*6
	print(round(t,1))