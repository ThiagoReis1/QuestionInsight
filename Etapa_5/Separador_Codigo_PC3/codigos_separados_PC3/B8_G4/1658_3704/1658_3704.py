from numpy import*
v = array(input("v: ")).upper() .split(',')

JPN=0
CHN=0
KOR=0
MGL=0
THA=0

for i in range(size(v)):
	if v[i] == JPN:
		JPN = JPN + 1
	elif v[i] == CHN:
		CHN = CHN + 1
	elif v[i] == KOR:
		KOR = KOR + 1
	elif v[i] == MGL:
		MGL = MGL + 1
	elif v[i] == THA:
		THA = THA + 1
print([JPN, CHN, KOR, MGL, THA])
		
	