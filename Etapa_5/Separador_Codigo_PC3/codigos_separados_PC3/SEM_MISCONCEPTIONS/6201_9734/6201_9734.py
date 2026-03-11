altura_joe = 1.77
taxa_joe = 0.02
altp = float(input("altura pessoa"))
taxap = float(input("taxa crescimento"))
anos = 0

while altp < altura_joe:
		altp += taxap
		altura_joe += taxa_joe
		anos +=1
print(anos)