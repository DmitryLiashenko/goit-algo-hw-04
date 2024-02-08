contacts = {'Dav' : 123, "asd" : 456 }


def show_phone(name, contacts):         # ФУНКЦИЯ ПОКАЗЫВАЕТ ТЕЛЕФОН ПО ИМЕНИ
    for key, value in contacts.items(): 
        if name == key:                 
            return key.get()  
# print(show_phone(Dav, contacts))


a = contacts.key.get(1)
print(a)