import random

table = {"клиенты": 0, "капитал": 10000, "производство": 0, "счёт в банке": 700,
         "место на рынке": 150, "цена товара": 10, "год": 0}
print(table["клиенты"], table["капитал"], table["производство"], table["счёт в банке"], table["место на рынке"],
      table["цена товара"], table["год"])
cost_advert = table["цена товара"] * 0.4
cost_made = table["цена товара"] / 3
message_1 = "Сколько произвести товара по цене " + str(round(cost_made)) + "$?"
message_2 = "Сколько клиентов привлечь по цене " + str(round(cost_advert)) + "$" + " за одного?"

percent = random.choice([x for x in range(70, 101)]) / 100
print(percent)
for year in range(1000):
    qs_1 = str(input(message_1))
    qs_2 = str(input(message_2))



