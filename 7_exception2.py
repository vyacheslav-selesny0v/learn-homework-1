"""

Домашнее задание №1

Исключения: приведение типов

* Перепишите функцию discounted(price, discount, max_discount=20)
  из урока про функции так, чтобы она перехватывала исключения,
  когда переданы некорректные аргументы.
* Первые два нужно приводить к вещественному числу при помощи float(),
  а третий - к целому при помощи int() и перехватывать исключения
  ValueError и TypeError, если приведение типов не сработало.
    
"""

def discounted(price, discount, max_discount=20):
    """
    Замените pass на ваш код
    """
    try:
        price = float(price)
        discount = float(discount)
        max_discount = int(max_discount)
    except ValueError:
        print('Ошибка значения')
    except TypeError:
        print('Ошибка типов аргументов')    
    
    if max_discount >= 100:
        raise ValueError("Слишком большая максимальная скидка")
        
    if discount >= max_discount:
        return price
    else:
        try:
            return price - (price * discount / 100)
        except TypeError:
            print('Ошибка типов аргументов')  # У меня срабатывает на этом print(discounted("five", 5))
        
if __name__ == "__main__":
    print(discounted(100, 2))
    print(discounted(100, "3"))
    print(discounted("100", "4.5"))
    print(discounted("five", 5))
    print(discounted("сто", "десять"))
    print(discounted(100.0, 5, "10"))
