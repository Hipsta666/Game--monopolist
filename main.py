import random


def advert(form, desk):
    cost_advert = form["цена товара"] * 0.6
    message_1 = "Сколько клиентов привлечь по цене " + str(round(cost_advert)) + "$" + " за одного?"
    qs_1 = int(input(message_1))
    start_capital = form["капитал"]
    form["капитал"] -= cost_advert * qs_1
    desk["привлечено"] = qs_1

    while form["капитал"] < 0:
        form["капитал"] = start_capital
        print("Нельзя столько клиентов привлечь, капитала не хватает!")
        qs_1 = int(input(message_1))
        form["капитал"] -= cost_advert * qs_1
        desk["привлечено"] = qs_1


def made(form, desk):
    if form["капитал"] > 0:
        cost_made = table["цена товара"] * 0.2
        message_2 = "Сколько произвести товара по цене " + str(round(cost_made)) + "$" + "?"
        qs_2 = int(input(message_2))
        desk["производство"] = qs_2
        form["капитал"] -= cost_made * qs_2
    else:
        print('Ой! У вас не хватает капитала.\n')
        cost_made = table["цена товара"] * 0.2
        cut_score(form)
        print('Отлично! У вас появились деньги!\n')
        message_2 = "Сколько произвести товара по цене " + str(round(cost_made)) + "$" + "?"
        qs_2 = int(input(message_2))
        form["капитал"] -= cost_made * qs_2


def presentation(form):
    print('|{:^6}|{:^12}|{:^16}|{:^16}|{:^10}|{:^10}|'.format('Год', 'Количество', 'Капитал', 'Счет', 'Место', 'Цена'))
    print('|{:^6}|{:^12}|{:^16}|{:^16}|{:^10}|{:^10}|'.format('', 'клиентов', '', 'в банке', 'на рынке', 'товара'))
    print('='*77)
    print('|{:^6}|{:^12}|{:^16}|{:^16}|{:^10}|{:^10}|'.format(form['год'], round(form["клиенты"]),
                                                        round(form["капитал"]), form["счёт в банке"],
                                                        form["место на рынке"], form["цена товара"],
                                                        form["год"]))
    print('-' * 77)


def score(form):
    percent = random.choice([item for item in range(110,120)]) / 100
    form["счёт в банке"] = round(form["счёт в банке"] * percent)
    return form


def year_change(form):
    form["год"] += 1


def cut_score(form):
    cut = int(input('Сколько денег вы хотите снять с вашего счета в банке?'))
    form["счёт в банке"] -= cut
    form["капитал"] += cut
    presentation(form)

def add_score(form):
    add = int(input('Сколько денег вы хотите положить на ваш счет в банке?'))
    form["капитал"] -= add
    form["счёт в банке"] += add
    presentation(form)


def free_production(form, desk):
    difference = desk["производство"] - form["клиенты"] * 2
    return difference


def adding_customers(form, desk):
    percent = random.choice([x for x in range(70, 101)]) / 100
    change = round(percent * desk["привлечено"])
    desk["потенциальные клиенты"] = change
    production_capability = round(free_production(form, desk) / 2)
    if (production_capability - change) < 0:
        form["клиенты"] += production_capability
        print("реклама сработала плохо, ушло " + str((-1) * production_capability) + " клиентов\n")
    elif (production_capability - change) >= 0:
        form["клиенты"] += change
        print("год прошел успешно, реклама смогла привлечь " + str(change) + " новых клиентов\n")


table = {'год': 0, "клиенты": 375, "капитал": 32500, "счёт в банке": 15000,
         "место на рынке": 148, "цена товара": 50}
cost_advert = table["цена товара"] * 0.6
presentation(table)


ddd = {"привлечено": 0, "производство": 0, "потенциальные клиенты": 0}

ddd = {"привлечено": 0}
table = {"клиенты": 375, "капитал": 32500, "счёт в банке": 15000,
         "место на рынке": 148, "цена товара": 50, "год": 0}


for year in range(1000):
    advert(table, ddd)
    made(table, ddd)
    free_production(table, ddd)
    adding_customers(table, ddd)
    year_change(table)
    score(table)
    presentation(table)
    add_score(table)

