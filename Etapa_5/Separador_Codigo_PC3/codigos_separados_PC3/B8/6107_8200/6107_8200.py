comb_cmn = float(input('combstivel comum: '))

if (comb_cmn > 0) and (comb_cmn < 17.5):
    total_comb = comb_cmn + 1.5
elif (comb_cmn >= 17.5) and (comb_cmn < 35):
    total_comb = comb_cmn + 2.3
elif (comb_cmn >= 35) and (comb_cmn < 50):
    total_comb = comb_cmn + 3.3
elif (comb_cmn >= 50):
    total_comb = comb_cmn + 4.7
print(round(total_comb,2))