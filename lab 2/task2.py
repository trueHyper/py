moneyCapital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

months = 0 
currentMoney = moneyCapital + salary 

while currentMoney >= spend: 
    months += 1
    spend *= (1 + increase) 
    currentMoney = salary - (spend - currentMoney)

print( months)
