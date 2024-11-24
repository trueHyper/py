salary = 5000  
spend = 6000  
months = 10
increase = 0.03

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

moneyCapital = 0

for i in range(months):
    if i > 0:
        spend *= (1 + increase)
    neededMoney = spend - salary 
    if neededMoney > 0:
        moneyCapital += neededMoney 

print(int(moneyCapital))
