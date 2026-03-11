merc = float(input())
taxa = 25.00
subt = merc * 43.21 + taxa
icms = subt * 0.62
total = subt + icms

print(round(total, 2))