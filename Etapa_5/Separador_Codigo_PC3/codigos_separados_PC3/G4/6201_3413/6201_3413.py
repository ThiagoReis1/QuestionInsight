

def maior():
	altura_joe = 1.77
	taxa_joe = 0.02
	alt = float(input())
	tax = float(input())
	count = 0
	
	while alt < altura_joe:
		alt += tax
		altura_joe += taxa_joe
		count += 1
	print(count)
	
maior()