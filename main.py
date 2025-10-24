# Словник для зберігання інформації про студентів
students = [
    {
        "group_number": "КН42/1",
        "full_name": "Анашкін Данило Андрійович",
        "course": 1,
        "semester": 1,
        "grades": {
            "Іноземна мова": 85,
            "Вища математика": 78,
            "Програмування": 90
        }
    },
    {
        "group_number": "КН42/1",
        "full_name": "Бондаренко Костянтин Олександрович",
        "course": 1,
        "semester": 1,
        "grades": {
            "Іноземна мова": 76,
            "Вища математика": 91,
            "Програмування": 88
        }
    },
    {
        "group_number": "КН42/1",
        "full_name": "Ганжара Богдан Сергійович",
        "course": 1,
        "semester": 1,
        "grades": {
            "Іноземна мова": 89,
            "Вища математика": 85,
            "Програмування": 86
        }
    }
]
# Функція Образцова Д.Є.
# Введення даних нового студента в список
def add_student(students_list):
    print("\nДодавання нового студента")

    # Введення даних студента
    group = input("Введіть номер групи: ").strip()
    name = input("Введіть ПІБ студента: ").strip()

    # Перевірка правильності введення курсу
    while True:
        try:
            course = int(input("введіть курс (1-6): ").strip())
            if 1 <= course <= 6: break
            print("Курс повинен бути в діапазоні 1-6")
        except ValueError:
            print("Введіть ціле число для курсу")
    # Перевірка правильності введення семестру
    while True:
        try:
            semester = int(input("Введіть семестр (1-12): ").strip())
            if 1 <= semester <= 12: break
            print("Семестр повинен бути в діапазоні 1-12")
        except ValueError:
            print("Введіть ціле число для семестру")

    # Введення оцінок з предметів
    print("\nВведіть оцінки з предметів:")
    grades = {}
    subjects = ["Іноземна мова", "Вища математика", "Програмування"]

    for subj in subjects:
        while True:
            try:
                g = int(input(f"{subj}: ").strip())
                if 0 <= g <= 100: grades[subj] = g; break
                print("Оцінка повинна бути від 0 до 100")
            except ValueError:
                print("Введіть ціле число для оцінки")

    # Додавання нового студента до списку
    students_list.append({
        "group_number": group,
        "full_name": name,
        "course": course,
        "semester": semester,
        "grades": grades
    })
    print(f"\nСтудента {name} додано до списку\n")


# функція Кіпренко П.А.
# виведення інформації про всіх студентів
def display_all_students(students_list):
    print("\nСписок студентів:")
    for s in students_list:
        print(f"\nПІБ: {s['full_name']}")
        print(f"Група: {s['group_number']}")
        print(f"Курс: {s['course']}")
        print(f"Семестр: {s['semester']}")
        print("Оцінки:")
        for subject, grade in s["grades"].items():
            print(f"    {subject}: {grade}")

def change_information(students_list):
    name = input("Введіть ПІБ студента: ").lower().strip()
    found_student = False

    for student in students_list:
        if student["full_name"].lower().strip() == name:
            found_student = True

            while True:
                print("\nЩо змінюємо?")
                print("1. Номер групи")
                print("2. Курс")
                print("3. Семестр")
                print("4. Оцінку")
                print("5. Завершити зміни")
                choice = input("Ваш вибір: ").strip()

                if choice == "1":
                    student["group_number"] = input("Введіть новий номер групи: ").strip()
                    print("Змінено номер групи!\n")
                elif choice == "2":
                    while True:
                        try:
                            student["course"] = int(input("Введіть новий курс: ").strip())
                            if 1<= student["course"] <= 6:
                                print("Змінено курс!\n")
                                break
                            else:
                                print("Курс від 1 до 6")
                        except ValueError:
                            print("Введіть число")
                elif choice == "3":
                    while True:
                        try:
                            student["semester"] = int(input("Введіть новий семестр: ").strip())
                            if 1 <= student["semester"] <= 12:
                                print("Змінено семестр!\n")
                                break
                            else:
                                print("Семестр від 1 до 12")
                        except ValueError:
                            print("Введіть число")
                elif choice == "4":
                    print("Доступні предмети:")
                    for subject in student["grades"]:
                        print(subject)
                    subj = input("Введіть назву предмета: ").strip()
                    if subj in student["grades"]:
                        while True:
                            try:
                                student["grades"][subj] = int(input("Нова оцінка: ").strip())
                                if 0 <= student["grades"][subj] <= 100:
                                    print("Оцінку змінено!\n")
                                    break
                                else:
                                    print("Оцінка від 0 до 100")
                            except ValueError:
                                print("Введіть число")
                    else:
                        print("Такого предмета немає.\n")
                elif choice == "5":
                    print("Повернення до головного меню\n")
                    return
                else:
                    print("Невірний вибір .\n")

    if not found_student:
        print("Студента не знайдено.\n")

 #меню
while True:
    print("Меню")
    print("1. Додати студента")
    print("2. Показати всіх студентів")
    print("3. Змінтити інформацію про студента")
    print("4. Вийти")
    choice = input("Оберіть дію: ").strip()

    if choice == "1":
        add_student(students)
    elif choice == "2":
        display_all_students(students)
    elif choice == "3":
        change_information(students)
    elif choice == "4":
        print("Завершення роботи програми"); break
    else:
        print("Неправильний вибір\n")
