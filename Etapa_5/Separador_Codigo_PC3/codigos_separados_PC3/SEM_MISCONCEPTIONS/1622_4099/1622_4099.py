from numpy import*

ent = array(eval(input("entraram: ")))
sai = array(eval(input("sairam: ")))

total = zeros(len(ent),dtype=int)

for i in range(len(ent)):
	total[i] = ent[i] - sai[i]

print(sum(total))