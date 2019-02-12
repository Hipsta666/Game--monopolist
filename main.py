import random


def advert(form, desk):
    cost_advert = form["цена товара"] * 0.6
    message_1 = "Сколько клиентов привлечь по цене " + str(round(cost_advert)) + "$" + " за одного?"
    qs_1 = int(input(message_1))
    form["капитал"] -= cost_advert * qs_1
    desk["привлечено"] = qs_1


def made(form):
    cost_made = table["цена товара"] * 0.2
    message_2 = "Сколько произвести товара по цене " + str(round(cost_made)) + "$"
    qs_2 = int(input(message_2))
    form["капитал"] -= cost_made * qs_2


def presentation(form):
    print('|{:^6}|{:^12}|{:^16}|{:^16}|{:^10}|{:^10}|'.format('Год','Количество','Капитал','Счет','Место','Цена'))
    print('|{:^6}|{:^12}|{:^16}|{:^16}|{:^10}|{:^10}|'.format('','клиентов','','в банке','на рынке','товара'))
    print('='*77)
    print('|{:^6}|{:^12}|{:^16}|{:^16}|{:^10}|{:^10}|'.format(form['год'],form["клиенты"],
                                                        round(form["капитал"]),form["счёт в банке"],
                                                        form["место на рынке"],form["цена товара"],
                                                        form["год"]))
    print('-' * 77)

def score(form):
    percent = random.choice([item for item in range(110,120)]) / 100
    form["счёт в банке"] *= percent
    return form

def change_score(money):
    cut = int(input('Сколько денег вы хотите снять с вашего счета в банке?'))
    money -= cut
    add = int(input('Сколько денег вы хотите положить на ваш счет в банке?'))
    money += add


table = {'год': 0, "клиенты": 375, "капитал": 32500, "счёт в банке": 15000,
         "место на рынке": 148, "цена товара": 50}
cost_advert = table["цена товара"] * 0.6


ddd = {"привлечено": 0}

table = {"клиенты": 375, "капитал": 32500, "счёт в банке": 15000,
         "место на рынке": 148, "цена товара": 50, "год": 0}


for year in range(1000):
    presentation(table)
    percent = random.choice([x for x in range(70, 101)]) / 100
    advert(table, ddd)
    made(table)
    print("год прошел успешно, реклама смогла привлечь " + str(percent * ddd["привлечено"]) + " новых клиентов")
    score(table)



