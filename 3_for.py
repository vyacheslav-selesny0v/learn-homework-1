"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
data = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]

def items_sum(items_sold):
        phone_sum = 0
        for quant in items_sold:
            phone_sum += quant    
        return phone_sum

def items_average(items_sold):
        phone_sum = 0
        for quant in items_sold:
            phone_sum += quant
        items_avg = phone_sum / len(items_sold)  
        return items_avg

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    
    for phone in data:
        total_phone_sum = items_sum(phone['items_sold'])
        print(f"Суммы проданных телефонов {phone['product']}: {total_phone_sum}")
        
    for phone in data:
        phone_items_avg = items_average(phone['items_sold'])
        print(f"Среднее число проданных телефонов {phone['product']}: {phone_items_avg}")

    total_sum = 0

    for phone in data:
        total_sum += items_sum(phone['items_sold'])
    print(f"Общая сумма проданных телефонов: {total_sum}")

    phone_items_avg_sum = 0

    for phone in data:
        phone_items_avg_sum += items_average(phone['items_sold'])

    phones_avg = phone_items_avg_sum / len(data)
    print(f"Среднее число проданных телефонов: {phones_avg}")

if __name__ == "__main__":
    main()
