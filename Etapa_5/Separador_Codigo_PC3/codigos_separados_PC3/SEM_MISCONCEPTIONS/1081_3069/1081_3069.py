pnota = float(input("primeiranota"))
snota = float(input("segundanota"))
tnota = float(input("terceiranota"))
qnota = float(input("quartanota"))
m = (pnota+snota+tnota+qnota)/4
print(round(m,2))
if (m >= 5):
	print("Aprovacao")
else:
	print("Reprovacao")