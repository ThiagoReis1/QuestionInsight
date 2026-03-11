amn = input()
O = 15.9994
C = 12.011
N = 14.0067
S = 32.066
H = 1.00794
if( "amn".lower == "aspartato" ):
	print(round((C * 4) + (H * 6) + (N)+ (O * 4) ,1))
else:
	print(round(( C * 3 ) + (H * 7) + (N) +(O * 2 ) + (S) ,1))