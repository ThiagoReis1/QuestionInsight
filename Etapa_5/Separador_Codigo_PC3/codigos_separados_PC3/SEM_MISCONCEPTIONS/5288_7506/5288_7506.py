age = int(input("Digite a idade: "))

count_minor = 0
count_total = 0 

while age != -1:
	if age < 18:
		count_minor += 1
	count_total += 1
	age = int(input("Digite a idade: "))
	
print(count_total)
print(round(100*count_minor/count_total, 2))