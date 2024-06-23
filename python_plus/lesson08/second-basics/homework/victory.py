# Словарь с известными людьми и их годами рождения
celebrities = {
    "Альберт Эйнштейн": 1879,   # Правильный ответ: 1879
    "Мария Кюри": 1867,         # Правильный ответ: 1867
    "Владимир Путин": 1952,     # Правильный ответ: 1952
    "Мадонна": 1958,            # Правильный ответ: 1958
    "Николас Кейдж": 1964       # Правильный ответ: 1964
}

def quiz():
    correct_answers = 0
    wrong_answers = 0
    
    print("Добро пожаловать в викторину! Ответьте на вопросы о годах рождения знаменитостей.")
    
    # Проходим по каждой знаменитости в словаре
    for celebrity, correct_year in celebrities.items():
        while True:
            try:
                user_answer = int(input(f"Введите год рождения {celebrity}: "))
                break
            except ValueError:
                print("Ошибка! Пожалуйста, введите год рождения числом.")
        
        # Проверяем ответ пользователя
        if user_answer == correct_year:
            print("Правильно!")
            correct_answers += 1
        else:
            print(f"Неправильно. Правильный ответ: {correct_year}")
            wrong_answers += 1
    
    total_questions = correct_answers + wrong_answers
    
    # Выводим статистику
    print("\nРезультаты викторины:")
    print(f"Количество правильных ответов: {correct_answers}")
    print(f"Количество ошибок: {wrong_answers}")
    print(f"Процент правильных ответов: {correct_answers * 100 / total_questions:.2f}%")
    print(f"Процент неправильных ответов: {wrong_answers * 100 / total_questions:.2f}%")

# Запуск викторины
while True:
    quiz()
    print("\nХотите начать игру заново? (да/нет)")
    restart = input().lower()
    if restart != 'да':
        print("Спасибо за игру! До свидания.")
        break