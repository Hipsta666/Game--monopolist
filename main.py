import random


def exception(message):
    """Исправляет ошибку при вводе не числа."""
    try:
        x = input(message)
        return int(x)
    except ValueError:
        print('Вы ввели не целое число. За вами уже выехали!')
        return exception(message)


def advert(form, desk):
    """Спрашивает у пользователя, сколько привлечь клиентов. Высчитывает, сколько будет привлечено.
    Отнимает затраты из капитала."""
    cost = desk["цена рекламы"]
    desk["цена товара"] = cost
    message_1 = "Сколько клиентов привлечь по цене " + str(round(cost)) + "$" + " за одного?"
    qs_1 = exception(message_1)
    start_capital = form["капитал"]
    form["капитал"] -= cost * qs_1
    desk["привлечено"] = qs_1

    while form["капитал"] < 0:
        form["капитал"] = start_capital
        print("Нельзя привлечь столько клиентов, капитала не хватает!!")
        qs_1 = exception(message_1)
        form["капитал"] -= cost * qs_1
        desk["привлечено"] = qs_1


def made(form, desk):
    """Спрашивает у пользователя, сколько товара произвести. Отнимает затраты из капитала."""
    if form["капитал"] > 0:
        cost_made = desk["цена производства"]
        message_2 = "Сколько произвести товара по цене " + str(round(cost_made)) + "$" + "?"
        qs_2 = exception(message_2)
        desk["производство"] = qs_2
        form["капитал"] -= cost_made * qs_2
    else:
        print('Ой! У вас не хватает капитала.\n')
        cost_made = form["цена товара"] * 0.2
        cut_score(form)
        print('Отлично! У вас появились деньги!\n')
        message_2 = "Сколько произвести товара по цене " + str(round(cost_made)) + "$" + "?"
        qs_2 = exception(message_2)
        form["капитал"] -= cost_made * qs_2


def presentation(form):
    """Вывод таблицы на данный момент."""
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
                                                                     'в банке, 10%',
                                                                     'на рынке',
                                                                     'спрос',
                                                                     'товара'))
    print('=' * 90)
    print('|{:^6}|{:^12}|{:^16}|{:^16}|{:^10}|{:^12}|{:^10}|'.format(
        form['год'],
        round(form["клиенты"]),
        str(round(form["капитал"])) + "$",
        str(round(form["счёт в банке"])) + "$",
        form["место на рынке"],
        round(form["количество людей"]),
        str(round(form["цена товара"])) + "$")
    )
    print('-' * 90)
    print("")


def score(form, desk):
    """Ежегодное увелечения счета в банке на процент."""
    """percent = random.choice([item for item in range(110, 120)]) / 100"""
    form["счёт в банке"] = round(form["счёт в банке"] * 1.1)


def year_change(form):
    """Счетчик года."""
    form["год"] += 1


def cut_score(form):
    """Спрашивает у пользователя, сколько денег снять со счета. Делает вычисления."""
    presentation(form)
    cut = exception('Денег не хватает! Сколько денег вы хотите снять с вашего счета в банке?')
    while cut < 0:
        cut = exception('Введите неотрицательное число:')
    while cut > form["счёт в банке"]:
        print("В банке нет столько денег!")
        cut = exception('Сколько денег вы хотите снять с вашего счета в банке?')
    form["счёт в банке"] -= cut
    form["капитал"] += cut


def bank_bankruptcy(form, desk):

    if form["год"] % 2 != 0:
        presentation(form)
        summ = round(form["счёт в банке"] * 0.3)
        message_T = "Вы можете застраховать свои деньги в банке, оплатив страховку. Сумма страховки в этот год "\
                    + str(summ) + "$" + "\n" + "Оплатить страховку? "
        a = input(message_T)
        while a not in "да,нет":
            a = input("Введите ответ (да/нет):")
        if a == "да":
            form["капитал"] -= summ
        else:
            desk["счётчик ответов НЕТ"] += 1
            if desk["счётчик ответов НЕТ"] % 2 == 0:
                print("Банк, где вы хранили деньги разорился. К сожалению, так как деньги были не застрахованы,"
                      "вы потеряли почти все свои сбережения. ")
                form["счёт в банке"] *= random.choice([0.1, 0.12, 0.13, 0.11, 0.14])


def add_score(form, desk):
    """Спрашивает у пользователя, сколько денег положить на счет. Делает вычисления."""
    add = exception('Сколько денег вы хотите положить на ваш счет в банке?')
    while add < 0:
        add = exception('Введите положительное число:')
    form["капитал"] -= add
    form["счёт в банке"] += add
    bank_bankruptcy(form, desk)


def free_production(form, desk):
    """Вычисляет разницу между количеством произведенного товара и количеством товаров, нужных потребителю."""
    difference = desk["производство"] - form["клиенты"] * 2
    return difference


def adding_customers(form, desk):
    """Вычисляет сколько клиентов привлечено или ушло."""
    percent = random.choice([x for x in range(70, 101)]) / 100
    change = round(percent * desk["привлечено"])
    desk["потенциальные клиенты"] = change
    production_capability = round(free_production(form, desk) / 2)

    if (production_capability - change) < 0:
        form["клиенты"] += production_capability
        form["капитал"] += form["клиенты"] * form["цена товара"]
        if production_capability < 0:
            print("Реклама сработала плохо, ушло " + str((-1) * production_capability) + " клиентов\n")
            desk["приход"] = production_capability
        elif production_capability == 0:
            print("Новых клиентов не прошло.")
            desk["приход"] = production_capability
        else:
            print("Год прошел успешно, реклама смогла привлечь " + str(production_capability) + " новых клиентов\n")
            desk["приход"] = production_capability
    elif (production_capability - change) >= 0:
        form["клиенты"] += change
        form["капитал"] += form["клиенты"] * form["цена товара"]
        if change < 0:
            print("Реклама сработала плохо, ушло " + str((-1) * change) + " клиентов\n")
            desk["приход"] = change
        elif change == 0:
            print("Новых клиентов не прошло.")
            desk["приход"] = change
        else:
            print("Год прошел успешно, реклама смогла привлечь " + str(change) + " новых клиентов\n")
            desk["приход"] = change


def negative_capital(form):
    """Вариант проигрыша."""
    while form["капитал"] < 0 and (-1) * form["капитал"] < form["счёт в банке"]:
        cut_score(form)
    if form["капитал"] < 0 and (-1) * form["капитал"] > form["счёт в банке"]:
        print("Вы проиграли!!!! Даже ваш счёт в банке не спасёт!")
        return True


def demand_add(form, desk, year):
    """Изменение прибывления спроса на рынке в зависимости от периодов."""
    if form["год"] >= year and year % 2 == 0:
        if year < 4:
            desk["спрос +от"] += 40
            desk["спрос +до"] += 40
        elif 4 <= year <= 6:
            desk["спрос +от"] += 180
            desk["спрос +до"] += 180
        elif 7 <= year <= 15:
            desk["спрос +от"] += 500
            desk["спрос +до"] += 555


def crisis(form, desk):
    """Событие - кризис."""
    a = desk["начальный капитал"]
    if str(form["год"]) in "3 7 5" and form["капитал"] > a * 2.5:
        print("Важное сообщение! На рынке ... произошёл кризис! К сожалению, он не обошёл вас стороной.\n"
              "В следствии чего вы потерпели потери клиентской базы, цена производства возрасла, как и цена рекламы,\n"
              "цена товара напротив - снизилась,\nтакже увеличилось количество покупателей на рынке! "
              "К несчастью, эти факторы повлияли на ваше место на рынке.\n"
              "Думаю, вы в силах с этим справиться!")
        form["клиенты"] *= 0.65
        desk["цена производства"] *= 1.5
        desk["цена рекламы"] *= 1.2
        form["цена товара"] *= 0.9
        form["количество людей"] *= 1.15
    if str(form["год"]) in "3 7 9" and form["капитал"] < a:
        print("Важное сообщение! На рынке ... произошёл кризис! Его действия коснулись и вас.\n"
              "Из-за чего вы понесли потери клиентской базы, цена производства и цена рекламы возрасла,\n"
              "цена товара напротив - снизилась, к тому же увеличилось количество покупателей на рынке!\n"
              "Все эти факторы повлияли на ваше место на рынке.\n")
        presentation(form)
        print("Решать только вам, уйти с рынка или остаться.")
        close = input("Уйти с рынка? ")
        while close != "нет" and close != "да":
            close = input("Введите ответ (да/нет):")
        if close == "да":
            desk["уйти с рынка"] = "да"
        else:
            form["клиенты"] *= 0.65
            desk["цена производства"] *= 2
            desk["цена рекламы"] *= 1.4
            form["цена товара"] *= 0.85
            form["количество людей"] *= 1.15


def demand(form, desk):
    """Изменения спроса на рынке с помощью метода рандом."""
    demand_add(form, desk, 2)
    add_1 = random.choice([x for x in range(desk["спрос +от"], desk["спрос +до"])])
    form["количество людей"] += add_1
    desk["изменение спроса"] = add_1


def place(form, desk):
    """Вычисляет место пользователя на рынке."""
    crisis(form, desk)
    demand(form, desk)
    change_1 = desk["приход"] - desk["изменение спроса"]
    if change_1 < 0 and change_1 <= (-1) * desk["изменение спроса"]:
        change_place = round(change_1 / 10)
        form["место на рынке"] -= change_place

    elif change_1 >= 0:
        change_place = round(change_1 / 10)
        form["место на рынке"] -= change_place


def cost_advert(form, desk):
    """Изменение стоимости рекламы."""
    desk["цена рекламы"] = random.choice([x for x in range(round(desk["цена рекламы"]) - 4,
                                                           round(desk["цена рекламы"]) + 5)])
    x = desk["начальное место"]
    y = desk["цена рекламы"]
    string_1 = "Вы понижаете свой рыночный рейтинг, рекламная компания решила сделать вам скидку на рекламу."
    string_2 = "Реклама работает успешно, поэтому рекламная компания подниамет цену на рекламу."
    if str(form["год"]) in "3 7 9" and form["место на рынке"] >= x:
        desk["цена рекламы"] = round(y * 0.8)
        print(string_1)
    if str(form["год"]) in "5 8" and form["место на рынке"] >= x:
        desk["цена рекламы"] = round(y * 0.7)
        print(string_1)
    if str(form["год"]) in "3 5 9" and form["место на рынке"] <= x * 0.9:
        desk["цена рекламы"] = round(y * 1.1)
        print(string_2)
    if str(form["год"]) in "7 8" and form["место на рынке"] <= x * 0.8:
        desk["цена рекламы"] = round(y * 1.1)
        print(string_2)


def monopolist(form, desk):
    """Все функции в совокупности."""
    presentation(form)
    for year in range(1000):
        cost_advert(form, desk)
        advert(form, desk)
        presentation(form)
        made(form, desk)
        negative_capital(form)
        free_production(form, desk)
        adding_customers(form, desk)
        place(form, desk)
        if desk["уйти с рынка"] == "да":
            print("Ты не справился с давлением рынка и проиграл...")
            break
        if form["место на рынке"] <= 1 or form["количество людей"] == form["клиенты"]:
            form["место на рынке"] = 1
            print("Ты стал монополистом, поздравляю!!!")
            presentation(form)
            break
        presentation(form)
        if form["клиенты"] <= 0:
            print("Ты проиграл!")
            break
        if negative_capital(form):
            break
        add_score(form, desk)
        year_change(form)
        score(form, desk)
        presentation(form)

    print("")


def main():
    """Основная функция. Выбор уровня сложности. Словари с начальными данными."""
    lvl = input("Выберите уровень сложности (лёгкий/сложный):")
    while lvl != "лёгкий" and lvl != "легкий" and lvl != "сложный":
        lvl = input("Выберите уровень сложности (лёгкий/сложный):")
    if lvl in "лёгкий легкий":
        table = {'год': 1, "клиенты": 201, "капитал": 25430, "счёт в банке": 12000,
                 "место на рынке": 158, "цена товара": 80, "количество людей": 6312}

        ddd = {"привлечено": 0, "производство": 0, "потенциальные клиенты": 0, "изменение спроса": 0, "приход": 0,
               "процент в банке": 1.10, "ушло клиентов": 0, "цена производства": 12,
               "цена рекламы": table["цена товара"] * 0.5, "спрос +от": 80, "спрос +до": 120,
               "начальное место": table["место на рынке"], "начальный капитал": table["капитал"],
               "счётчик ответов НЕТ": 0, "уйти с рынка": "нет"}
        monopolist(table, ddd)
    elif lvl == "сложный":
        table = {'год': 1, "клиенты": 375, "капитал": 36800, "счёт в банке": 15000,
                 "место на рынке": 831, "цена товара": 70, "количество людей": 15990}

        ddd = {"привлечено": 0, "производство": 0, "потенциальные клиенты": 0, "изменение спроса": 0, "приход": 0,
               "процент в банке": 1.10, "ушло клиентов": 0, "цена производства": 14,
               "цена рекламы": table["цена товара"] * 0.6, "спрос +от": 150, "спрос +до": 250,
               "начальное место": table["место на рынке"], "начальный капитал": table["капитал"],
               "счётчик ответов НЕТ": 0, "уйти с рынка": "нет"}
        monopolist(table, ddd)


main()