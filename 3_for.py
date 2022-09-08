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

def calculation_of_phones(number_of_phones):
    product_sum = 0
    for product in number_of_phones:
            
        product_sum = sum(number_of_phones)
        
        return product_sum

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    
    all_product_sum = 0
    
    for phone in data:
        phones_sum = calculation_of_phones(phone['items_sold'])
        print(f"Суммы проданных телефонов {phone['product']}: {phones_sum}")
        product_avg = calculation_of_phones(phone['items_sold'])/len(phone['items_sold'])
        print(f"Среднее кол-во проданных телефонов {phone['product']}: {product_avg}")
        all_product_sum += phones_sum
        all_product_avg = all_product_sum/len(data)
    print(f"Общее кол-во проданных телефонов: {all_product_sum}")
    print(f"Среднее кол-во проданных телефонов: {all_product_avg}")    
if __name__ == "__main__":
    main()
