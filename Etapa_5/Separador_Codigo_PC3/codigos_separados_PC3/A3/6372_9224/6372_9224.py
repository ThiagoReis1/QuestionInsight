from numpy import*

itens = input(":").split(",")
count = zeros(4,dtype=int)
i = 0
total = 0

for i in range(size(itens)):
	if itens[i] == "A":
		count[0] = count[0] + 1
	if itens[i] == "B":
	 	count[1] = count[1] + 1
	if itens[i] == "L":
	   count[2] = count[2] + 1
	if itens[i] == "H":
	   count[3] = count[3] + 1
print(count)