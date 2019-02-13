import random


def advert(form, desk):
    cost = form["цена товара"] * 0.6
    message_1 = "Сколько клиентов привлечь по цене " + str(round(cost)) + "$" + " за одного?"
    qs_1 = int(input(message_1))
    start_capital = form["капитал"]
    form["капитал"] -= cost * qs_1
    desk["привлечено"] = qs_1

    while form["капитал"] < 0:
        form["капитал"] = start_capital
        print("Нельзя столько клиентов привлечь, капитала не хватает!")
        qs_1 = int(input(message_1))
        form["капитал"] -= cost * qs_1
        desk["привлечено"] = qs_1


def made(form, desk):
    if form["капитал"] > 0:
        cost_made = form["цена товара"] * 0.2
        message_2 = "Сколько произвести товара по цене " + str(round(cost_made)) + "$" + "?"
        qs_2 = int(input(message_2))
        desk["производство"] = qs_2
        form["капитал"] -= cost_made * qs_2
    else:
        print('Ой! У вас не хватает капитала.\n')
        cost_made = form["цена товара"] * 0.2
        cut_score(form)
        print('Отлично! У вас появились деньги!\n')
        message_2 = "Сколько произвести товара по цене " + str(round(cost_made)) + "$" + "?"
        qs_2 = int(input(message_2))
        form["капитал"] -= cost_made * qs_2


def presentation(form):
    print("")
    print('|{:^6}|{:^12}|{:^16}|{:^16}|{:^10}|{:^12}|{:^10}|'.format('Год', 'Количество', 'Капитал', 'Счет', 'Место','Рыночный', 'Цена'))
    print('|{:^6}|{:^12}|{:^16}|{:^16}|{:^10}|{:^12}|{:^10}|'.format('', 'клиентов', '', 'в банке' + " 10%", 'на рынке','спрос', 'товара'))
    print('='*90)
    print('|{:^6}|{:^12}|{:^16}|{:^16}|{:^10}|{:^12}|{:^10}|'.format(form['год'], round(form["клиенты"]),
                                                        round(form["капитал"]), form["счёт в банке"],
                                                        form["место на рынке"], form["количество людей"],form["цена товара"]))
    print('-' *90)
    print("")


def score(form, desk):
    '''percent = random.choice([item for item in range(110, 120)]) / 100'''
    form["счёт в банке"] = round(form["счёт в банке"] * 1.1)


def year_change(form):
    form["год"] += 1


def cut_score(form):
    cut = int(input('Денег не хватает! Сколько денег вы хотите снять с вашего счета в банке?'))
    while cut > form["счёт в банке"]:
        print("В банке нет столько денег!")
        cut = int(input('Сколько денег вы хотите снять с вашего счета в банке?'))
    form["счёт в банке"] -= cut
    form["капитал"] += cut
    presentation(form)


def add_score(form):
    add = int(input('Сколько денег вы хотите положить на ваш счет в банке?'))
    form["капитал"] -= add
    form["счёт в банке"] += add


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
        form["капитал"] += form["клиенты"] * form["цена товара"]
        if production_capability < 0:
            print("реклама сработала плохо, ушло " + str((-1) * production_capability) + " клиентов\n")
            desk["приход"] = production_capability
        else:
            print("год прошел успешно, реклама смогла привлечь " + str(production_capability) + " новых клиентов\n")
            desk["приход"] = production_capability
    elif (production_capability - change) >= 0:
        form["клиенты"] += change
        form["капитал"] += form["клиенты"] * form["цена товара"]
        if change < 0:
            print("реклама сработала плохо, ушло " + str((-1) * change) + " клиентов\n")
            desk["приход"] = change
        else:
            print("год прошел успешно, реклама смогла привлечь " + str(change) + " новых клиентов\n")
            desk["приход"] = change


def negative_capital(form):
    while form["капитал"] < 0 and (-1) * form["капитал"] < form["счёт в банке"]:
        cut_score(form)
    if form["капитал"] < 0 and (-1) * form["капитал"] > form["счёт в банке"]:
        print("Вы проиграли!!!! Даже ваш счёт в банке не спасёт!")
        return True


def demand(form, desk):
    add_1 = random.choice([x for x in range(150, 250)])
    form["количество людей"] += add_1
    desk["изменение спроса"] = add_1


def place(form, desk):
    demand(form, desk)
    change_1 = desk["приход"] - desk["изменение спроса"]
    if change_1 < 0 and change_1 <= (-1) * desk["изменение спроса"]:
        change_place = round(change_1 / 10)
        form["место на рынке"] -= change_place

    elif change_1 >= 0:
        change_place = round(change_1 / 10)
        form["место на рынке"] -= change_place


def main():
    table = {'год': 0, "клиенты": 375, "капитал": 32500, "счёт в банке": 15000,
             "место на рынке": 148, "цена товара": 60, "количество людей": 20000}

    ddd = {"привлечено": 0, "производство": 0, "потенциальные клиенты": 0, "изменение спроса": 0, "приход": 0,
           "процент в банке": 1.10, "ушло клиентов": 0}

    presentation(table)

    for year in range(1000):
        advert(table, ddd)
        presentation(table)
        made(table, ddd)
        presentation(table)
        negative_capital(table)
        free_production(table, ddd)
        adding_customers(table, ddd)
        place(table, ddd)
        year_change(table)
        score(table, ddd)
        presentation(table)
        if table["клиенты"] <= 0:
            print("Ты проиграл!")
            break
        if negative_capital(table):
            break
        add_score(table)
        presentation(table)


main()