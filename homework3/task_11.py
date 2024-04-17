phone_book = []

while True:
    print("\n\t Телефонная книга")
    print("1. Добавить новый контакт")
    print("2. Удалить контакт")
    print("3. Просмотреть все имена контактов")
    print("4. Просмотреть информацию о конкретном контакте")
    print("5. Выйти из программы")
    choice = input("Выберите действие (1-5): ")

    if choice == "1":
        name = input("Введите имя нового контакта: ")
        if any(contact['name'] == name for contact in phone_book):
            print("Контакт с таким именем уже существует, попробуйте другое имя")
        else:
            phone = input("Введите номер нового контакта: ")
            mail = input("Введите Email нового контакта: ")
            phone_book.append({"name": name, "phone": phone, "mail": mail})
            print("Контакт успешно добавлен")
    
    elif choice == "2":
        name_to_remove = input("Введите имя контакта для удаления: ")
        found_contact = [contact for contact in phone_book if contact['name'] == name_to_remove]
        if not found_contact:
            print("Контакт не найден")
        else:
            print(f"Вы действительно хотите удалить контакт {name_to_remove}?")
            confirm = input("Введите 'Да' для подтверждения или 'Нет' для отмены: ")
            if confirm.lower() == "да":
                phone_book = [contact for contact in phone_book if contact['name'] != name_to_remove]
                print("Контакт успешно удалён.")
            else:
                print("Удаление отменено.")
            
    elif choice == "3":
        if phone_book:
            print("\n\tСписок всех контактов: ")
            for idx, contact in enumerate(phone_book, 1):
                print(f"{idx}. {contact['name']}")
        else:
            print("Телефонная книга пуста.")

    elif choice == "4":
        contact_to_view = input("Введите имя контакта о котором хотите узнать информацию: ")
        for contact in phone_book:
            if contact['name'] == contact_to_view:
                print(f"Имя: {contact['name']}; Телефон: {contact['phone']}; Почта: {contact['mail']}")
                break
        else:
            print('Контакт не найден')

    elif choice == "5":
        print("Выход из программы.")
        break
    
    else:
        print("Неверный ввод. Пожалуйста, введите число от 1 до 5.")

    
