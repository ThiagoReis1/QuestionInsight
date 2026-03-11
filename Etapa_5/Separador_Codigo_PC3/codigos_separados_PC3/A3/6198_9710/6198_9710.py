altura_luna = 1.65
taxa_luna = 0.02
taxa_cresc_luna=0.02
altura_outro = float (input())
taxa_outro = float(input())
anos = 0
while altura_outro<= altura_luna:
	altura_luna += taxa_luna
	altura_outro += taxa_outro
	anos += 1
print(anos)