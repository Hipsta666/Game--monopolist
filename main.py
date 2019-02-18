import random


def advert(form, desk):
    cost = desk["цена рекламы"]
    desk["цена товара"] = cost
    message_1 = "Сколько клиентов привлечь по цене " + str(round(cost)) + "$" + " за одного?"
    qs_1 = int(input(message_1))
    start_capital = form["капитал"]
    form["капитал"] -= cost * qs_1
    desk["привлечено"] = qs_1

    while form["капитал"] < 0:
        form["капитал"] = start_capital
        print("Нельзя привелечь столько клиентов, капитала не хватает!")
        qs_1 = int(input(message_1))
        form["капитал"] -= cost * qs_1
        desk["привлечено"] = qs_1


def made(form, desk):
    if form["капитал"] > 0:
        cost_made = desk["цена производства"]
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
    print('|{:^6}|{:^12}|{:^16}|{:^16}|{:^10}|{:^12}|{:^10}|'.format('Год',
                                                                     'Количество',
                                                                     'Капитал',
                                                                     'Счет',
                                                                     'Место',
                                                                     'Рыночный',
                                                                     'Цена'))
    print('|{:^6}|{:^12}|{:^16}|{:^16}|{:^10}|{:^12}|{:^10}|'.format('',
                                                                     'клиентов',
                                                                     '',
                                                                     'в банке' + " 10%",
                                                                     'на рынке',
                                                                     'спрос',
                                                                     'товара'))
    print('=' * 90)
    print('|{:^6}|{:^12}|{:^16}|{:^16}|{:^10}|{:^12}|{:^10}|'.format(
        form['год'],
        round(form["клиенты"]),
        round(form["капитал"]),
        form["счёт в банке"],
        form["место на рынке"],
        form["количество людей"],
        form["цена товара"])
    )
    print('-' * 90)
    print("")


def score(form, desk):
    '''percent = random.choice([item for item in range(110, 120)]) / 100'''
    form["счёт в банке"] = round(form["счёт в банке"] * 1.1)


def year_change(form):
    form["год"] += 1


def cut_score(form):
    presentation(form)
    cut = int(input('Денег не хватает! Сколько денег вы хотите снять с вашего счета в банке?'))

    while cut > form["счёт в банке"]:
        print("В банке нет столько денег!")
        cut = int(input('Сколько денег вы хотите снять с вашего счета в банке?'))
    form["счёт в банке"] -= cut
    form["капитал"] += cut


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
        if production_capability <= 0:
            print("реклама сработала плохо, ушло " + str((-1) * production_capability) + " клиентов\n")
            desk["приход"] = production_capability
        else:
            print("год прошел успешно, реклама смогла привлечь " + str(production_capability) + " новых клиентов\n")
            desk["приход"] = production_capability
    elif (production_capability - change) >= 0:
        form["клиенты"] += change
        form["капитал"] += form["клиенты"] * form["цена товара"]
        if change <= 0:
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


def demand_add(form, desk, year):
    if form["год"] >= year and year % 2 == 0:
        if year < 11:
            desk["спрос +от"] += 70
            desk["спрос +до"] += 70
        elif 11 <= year <= 21:
            desk["спрос +от"] += 140
            desk["спрос +до"] += 140


def demand(form, desk):
    demand_add(form, desk, 4)
    add_1 = random.choice([x for x in range(desk["спрос +от"], desk["спрос +до"])])
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


def cost_advert(form, desk):
    desk["цена рекламы"] = random.choice([x for x in range(round(desk["цена рекламы"]) - 2,
                                                           round(desk["цена рекламы"]) + 2)])
    x = desk["начальное место"]
    y = desk["цена рекламы"]
    string_1 = "Вы понижаете свой рыночный рейтинг, рекламная компания решила сделать вам скидку на рекламу."
    string_2 = "Реклама работает успешно, поэтому рекламная компания подниамет цену на рекламу."
    if form["год"] == 5 and form["место на рынке"] >= x:
        desk["цена рекламы"] = round(y * 0.8)
        print(string_1)
    if form["год"] == 7 and form["место на рынке"] >= x:
        desk["цена рекламы"] = round(y * 0.7)
        print(string_1)
    if form["год"] == 5 and form["место на рынке"] <= x * 0.9:
        desk["цена рекламы"] = round(y * 1.1)
        print(string_2)
    if form["год"] == 9 and form["место на рынке"] >= x * 0.8:
        desk["цена рекламы"] = round(y * 1.1)
        print(string_2)


def monopolist(form, desk):
    presentation(form)
    for year in range(1000):
        cost_advert(form, desk)         # Собитие - рыночный рейтинг падает
        """
        
        
        Тут должны быть функции событий
        
        
        """
        advert(form, desk)
        presentation(form)
        made(form, desk)
        negative_capital(form)
        free_production(form, desk)
        adding_customers(form, desk)
        place(form, desk)
        if form["место на рынке"] <= 1 or form["количество людей"] == form["клиенты"]:
            form["место на рынке"] = 1
            print("Ты стал монополистом, поздравляю!!!")
            presentation(form)
            break
        year_change(form)
        print(desk["спрос +от"], desk["спрос +до"])
        score(form, desk)
        presentation(form)
        if form["клиенты"] <= 0:
            print("Ты проиграл!")
            break
        if negative_capital(form):
            break
        add_score(form)
        presentation(form)


def main():
    lvl = input("Выберите уровень сложности (лёгкий/сложный):")
    while lvl not in "лёгкий легкий сложный":
        lvl = input("Выберите уровень сложности (лёгкий/сложный):")
    if lvl in "лёгкий легкий":
        table = {'год': 0, "клиенты": 201, "капитал": 25430, "счёт в банке": 12000,
                 "место на рынке": 158, "цена товара": 80, "количество людей": 6312}

        ddd = {"привлечено": 0, "производство": 0, "потенциальные клиенты": 0, "изменение спроса": 0, "приход": 0,
               "процент в банке": 1.10, "ушло клиентов": 0, "цена производства": table["цена товара"] * 0.15,
               "цена рекламы": table["цена товара"] * 0.5, "спрос +от": 80, "спрос +до": 120,
               "начальное место": table["место на рынке"]}
        monopolist(table, ddd)
    if lvl == "сложный":
        table = {'год': 0, "клиенты": 375, "капитал": 36800, "счёт в банке": 15000,
                 "место на рынке": 831, "цена товара": 70, "количество людей": 15990}

        ddd = {"привлечено": 0, "производство": 0, "потенциальные клиенты": 0, "изменение спроса": 0, "приход": 0,
               "процент в банке": 1.10, "ушло клиентов": 0, "цена производства": table["цена товара"] * 0.2,
               "цена рекламы": table["цена товара"] * 0.6, "спрос +от": 150, "спрос +до": 250,
               "начальное место": table["место на рынке"]}
        monopolist(table, ddd)


main()
