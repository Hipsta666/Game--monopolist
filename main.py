import random




def advert(num, cost, form):
    form["капитал"] = form["капитал"] - num * cost


def presentation(form):
    print(form["клиенты"], round(form["капитал"]), form["производство"], form["счёт в банке"], form["место на рынке"],
          form["цена товара"], form["год"])


table = {"клиенты": 0, "капитал": 10000, "производство": 0, "счёт в банке": 700,
         "место на рынке": 150, "цена товара": 50, "год": 0}
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



