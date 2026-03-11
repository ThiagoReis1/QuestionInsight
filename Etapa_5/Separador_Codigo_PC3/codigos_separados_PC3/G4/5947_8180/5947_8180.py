sal = input("coxinha ou esfirra(C/E): ")
q1 = int(input("qual a quantidade de sal: "))
q2 = int(input("qual a quantidade do suco: "))
C = 2.00
E = 4.50
S = 6.00
if (sal == "C"):
	cal = (((C) * (q1)) + ((S) * (q2)))
else:
	cal = (((E) * (q1)) + ((S) * (q2)))
print(round(cal, 2))