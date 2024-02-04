def parse_input(user_input):            # ФУНКЦИЯ ПАРСЕРА КОМАНД           
    cmd, *args = user_input.split()     # РАЗДЕЛЯЕМ ВВОД НА КОМАНДУ И АРГУМЕНТЫ
    cmd = cmd.strip().lower()           # ПРИВОДИМ В НИЖНИЙ РЕГИСТР И УДАЛЯЕМ ЛИШНИИ ПРОБЕЛЫ
    return cmd, *args                   # ВОЗВРАЩАЕМ КОМАНДУ И СПИСОК АРГУМЕНТОВ

def add_contact(args, contacts):        # ФУНКЦИЯ ДОБАВЛЕНИЯ КОНТАКТОВ
    name, phone = args                  # ПРИСВАИВАЕМ АРГУМЕНТЫ ИМЕНИ И ТЕЛЕФОНУ
    contacts[name] = phone              # ЗАНОСИМ В СЛОВАРЬ ПО КЛЮЧЮ ТЕЛЕФОН
    return "Contact added."             #

def change_contact(args, contacts):     # ФУНКЦИЯ ИЗМЕНЕНИЯ КОНТАКТА
    name, phone = args
    for key, value in contacts.items(): # ПРОХОДИМСЯ ПО СЛОВАРЮ
        if key == name:                 # ЕСЛИ КЛЮЧ СОВПАДАЕТ С ИМЕНЕМ 
            contacts[name] = phone      # ПРИСВАИВАЕМ ИМЕНИ НОВЫЙ ТЕЛЕФОН
    return "Contact change"

def show_phone(args, contacts):         # ФУНКЦИЯ ПОКАЗЫВАЕТ ТЕЛЕФОН ПО ИМЕНИ
    name = args
    for key, value in contacts.items(): 
        if name == key:                 
            return value                # ВОЗВРАЩАЕМ ЗНАЧЕНИЕ НАЙДЕНОЕ ПО КЛЮЧУ
    

def show_all(contacts=None):       # ФУНКЦИЯ ВЫВОДИТ ВСЕ КОНТАКТЫ В СЛОВАРЕ(ДОБАВИТЬ \n)
    return contacts
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")  # ПОЛУЧАЕМ КОМАНДУ
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:         # БЛОК ВЫХОДА
            print("Good bye!")
            break 
        elif command == "hello":                 # ПРИВЕТСТВИЕ
            print("How can I help you?")
        elif command == "add":                   # ДОБАВЛЕНИЕ КОНТАКТА
            print(add_contact(args, contacts))
        elif command == "change":                # СМЕНА КОНТАКТА
             print(change_contact(args, contacts))
        elif command == "phone":                 # ПОКАЗЫВАЕТ КОНТАКТ ПО ИМЕНИ
            print(show_phone(args, contacts))
        elif command == "all":                   # ПОКАЗЫВВАЕМ ВЕСЬ СЛОВАРЬ
            print(show_all(contacts)) 
        else:                                    # СООБЩАЕМ О НЕ ПРАВИЛЬНОЙ КОМАНДЕ
            print("Invalid command.")

if __name__ == "__main__":
    main()