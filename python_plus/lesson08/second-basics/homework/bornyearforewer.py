correct_year = 1799
correct_day = 6

while True:

    year = input("Введите год рождения А.С. Пушкина: ")


    if not year.isdigit():
        print("Неверный год")
    else:
        year = int(year)

        if year == correct_year:

            day = input("Введите день рождения А.С. Пушкина (число от 1 до 31): ")
            
            if not day.isdigit():
                print("Неверный день рождения")
            else:
                day = int(day)

                if day == correct_day:
                    print("Верно")
                    break
                else:
                    print("Неверный день рождения")
        else:
            print("Неверный год")