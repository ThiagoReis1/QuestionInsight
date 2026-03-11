altura_luna = 1.65
taxa_luna = 0.02

altura1 = float(input("altura:"))
taxa1 = float(input("taxa:"))
ano = 0

while altura1 <= altura_luna:
	altura_luna += taxa_luna
	altura1 += taxa1
	ano += 1
	
print(ano)