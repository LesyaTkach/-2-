salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
for month in range(months):
    # Рассчитываем расходы текущего месяца
    if month > 0:  # Для первого месяца рост не применяется
        spend *= (1 + increase)
    deficit = spend - salary

    # Если есть нехватка, добавляем её к подушке безопасности
    if deficit > 0:
        money_capital += deficit

money_capital = round(money_capital)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
