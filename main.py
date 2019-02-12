import random




def advert(num, cost, form):
    form["капитал"] = form["капитал"] - num * cost


def presentation(form):
    print('|{:^6}|{:^12}|{:^16}|{:^16}|{:^10}|{:^10}|'.format('Год','Количество','Капитал','Счет','Место','Цена'))
    print('|{:^6}|{:^12}|{:^16}|{:^16}|{:^10}|{:^10}|'.format('','клиентов','','в банке','на рынке','товара'))
    print('='*77)
    print('|{:^6}|{:^12}|{:^16}|{:^16}|{:^10}|{:^10}|'.format(form['год'],form["клиенты"],
                                                        round(form["капитал"]),form["счёт в банке"],
                                                        form["место на рынке"],form["цена товара"],
                                                        form["год"]))
    print('-' * 77)

def score(money):
    percent = random.choice([item for item in range(110,120)]) / 100
    money *= percent
    return money


table = {'год': 0, "клиенты": 375, "капитал": 32500, "счёт в банке": 15000,
         "место на рынке": 148, "цена товара": 50}
presentation(table)
cost_advert = table["цена товара"] * 0.6


cost_made = table["цена товара"] * 0.2
message_1 = "Сколько клиентов привлечь по цене " + str(round(cost_advert)) + "$" + " за одного?"
message_2 = "Сколько произвести товара по цене " + str(round(cost_made)) + "$"

percent = random.choice([x for x in range(70, 101)]) / 100
for year in range(1000):
    qs_1 = int(input(message_1))
    advert(qs_1, cost_advert, table)
    presentation(table)
    qs_2 = int(input(message_2))
    score()


