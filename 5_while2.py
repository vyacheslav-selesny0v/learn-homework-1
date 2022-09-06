"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

questions_and_answers = {'Как дела?': 'Отлично', 'Что делаешь?': 'Программирую', 'Сколько уже занимаешься?': '2 дня'}

def ask_user(questions_and_answers):

    user_say = input('Введите ваш вопрос ')
    
    while user_say in questions_and_answers:
        
        if user_say in questions_and_answers:
            print(questions_and_answers[user_say])
        else:
            break
    
if __name__ == '__main__':
    ask_user(questions_and_answers)
