def parse_input(user_input):        #ФУНКЦИЯ ПАРСЕРА КОМАНД           
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):    # ФУНКЦИЯ ДОБАВЛЕНИЯ КОНТАКТОВ
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact():
    return "Contact change"

def show_phone():
    pass

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
        elif command == "change":                # 
             print(change_contact())
        elif command == "phone":                 # 
            print(show_phone())
        elif command == "all":                   # ПОКАЗЫВВАЕМ ВЕСЬ СЛОВАРЬ
            print(show_all(contacts)) 
        else:                                    # СООБЩАЕМ О НЕ ПРАВИЛЬНОЙ КОМАНДЕ
            print("Invalid command.")

if __name__ == "__main__":
    main()