# faça seu código aqui!
quant = int(input())
c = input()

total = quant * 40

if c == "s":
	total = total - (total* 0.05)

print(round(total, 1))