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
    name  = input("Введіть ПІБ студента: ").strip()

    # Перевірка правильності введення курсу
    while True:
        try:
            course = int(input("введіть курс (1-6): ").strip())
            if 1 <= course <= 6: break
            print("Курс повинен бути в діапазоні 1-6")
        except ValueError: print("Введіть ціле число для курсу")
    # Перевірка правильності введення семестру
    while True:
        try:
            semester = int(input("Введіть семестр (1-12): ").strip())
            if 1 <= semester <= 12: break
            print("Семестр повинен бути в діапазоні 1-12")
        except ValueError: print("Введіть ціле число для семестру")

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
            except ValueError: print("Введіть ціле число для оцінки")
    
    # Додавання нового студента до списку
    students_list.append({
        "group_number": group,
        "full_name":    name,
        "course":       course,
        "semester":     semester,
        "grades":       grades
    })
    print(f"\nСтудента {name} додано до списку\n")


# Меню 
while True:
    print("Меню")
    print("1. Додати студента")
    print("2. Вийти")
    choice = input("Оберіть дію: ").strip()

    if choice == "1": add_student(students)

    elif choice == "2": print("Завершення роботи програми"); break
    else: print("Неправильний вибір\n")
