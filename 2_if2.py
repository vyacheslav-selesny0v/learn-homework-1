"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main(first_string, second_string):
    
    if type(first_string) != str or type(second_string) != str:
        return 0
            
    if first_string == second_string:
        return 1
            
    if len(first_string) > len(second_string):
        return 2
            
    if second_string == 'learn':
        return 3
        
if __name__ == "__main__":
    print(main('safdaf', 2))
    print(main('aaaa', 'aaaa'))
    print(main('aaaa', 'a'))
    print(main('aaa', 'learn'))