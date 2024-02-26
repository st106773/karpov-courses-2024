def final_balance(init_sum, interest_rate, years, round_num=2):
    balance = init_sum * ((100 + interest_rate)/100) ** years
    return round(balance, round_num)

per = [
    (1000, 5, 10),
    (700, 7 , 10),
]
for p in per:
    init_sum, interest_rate, years = p
result = final_balance(init_sum, interest_rate, years, round_num=2)
print(result)
