hora = int(input())
taxa = hora * 15 + 5
icms = 20/100
total = taxa + taxa * icms
print(round(total, 2))
