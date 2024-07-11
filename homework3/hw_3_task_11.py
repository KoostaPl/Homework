# Создаем словарь для хранения контактов
phone_book = {}

while True:
    print("\n\tТелефонная книга")
    print("1. Добавить контакт")
    print("2. Удалить контакт")
    print("3. Просмотреть все контакты")
    print("4. Просмотреть информацию о контакте")
    print("5. Выйти из программы")

    choice = input("Выберите действие (введите номер): ")

    if choice == "1":
        name = input("Введите имя нового контакта: ")
        if name in phone_book:
            print("Контакт с таким именем уже существует")
        else:
            phone = input("Введите номер телефона: ")
            mail = input("Введите почту: ")
            phone_book[name] = {"phone": phone, "mail": mail}
            print("Контакт успешно добавлен")

    elif choice == "2":
        name_to_remove = input("Введите имя контакта для удаления: ")
        if name_to_remove in phone_book:
            del phone_book[name_to_remove]
            print("Контакт успешно удалён.")
        else:
            print("Контакт не найден")

    elif choice == "3":
        if phone_book:
            print("\n\tСписок всех контактов: ")
            for idx, name in enumerate(phone_book, 1):
                print(f"{idx}. {name}")
        else:
            print("Телефонная книга пуста.")

    elif choice == "4":
        contact_to_view = input(
            "Введите имя контакта о котором хотите узнать информацию: "
        )
        if contact_to_view in phone_book:
            contact_info = phone_book[contact_to_view]
            print(
                f"Имя: {contact_to_view}; Телефон: {contact_info['phone']}; "
                f"Почта: {contact_info['mail']}"
            )
        else:
            print("Контакт не найден")

    elif choice == "5":
        print("Выход из программы.")
        break

    else:
        print("Неверный ввод. Пожалуйста, введите число от 1 до 5.")
