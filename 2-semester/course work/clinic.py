#Импорт модуля для работы с файловой системой
import os

#Название для создания базы данных клиники
database_file = "clinic_database.txt" 

#Функция для загрузки данных из файла база данных
def load_database():
    #Создание словаря
    database = {}
    #Проверка существует ли файл
    if os.path.exists(database_file):
        with open(database_file, "r", encoding="utf-8") as file:
            for line in file:
                #Проверка, что строка не пустая
                if line.strip():  
                    #Создание списка разделенных знаком ";"
                    entry = line.strip().split(";")
                    #Создание ключа для словаря
                    key = entry[0].strip()
                    #Создание значения для словаря
                    value = {
                        "specialist": entry[1].strip(),
                        "appointment_time": entry[2].strip(),
                        "policy_number": entry[3].strip()
                    }
                    database[key] = value
    return database

#Функция для сохранения данных в файл
def save_database(database):
    with open(database_file, "w", encoding="utf-8") as file:
        for key, value in database.items():
            line = f"{key};{value['specialist']};{value['appointment_time']};{value['policy_number']}\n"
            file.write(line)

#Функция для вывода содержимого базы данных
def print_database(database):
    #Проверка существует ли база данных
    if not database:
        print("База данных пуста.")
    else:
        for key, value in database.items():
            print(f"Ф.И.О.: {key}")
            print(f"Принимающий специалист: {value['specialist']}")
            print(f"Время приема: {value['appointment_time']}")
            print(f"Номер полиса: {value['policy_number']}")
            print()

#Функция для добавления новый записей в базу данных
def add_entry(database, full_name, specialist, appointment_time, policy_number):
    database[full_name] = {
        "specialist": specialist,
        "appointment_time": appointment_time,
        "policy_number": policy_number
    }
    save_database(database)

#Функция для удаления записей в базе данных по ФИО 
def delete_entry(database, full_name):
    if full_name in database:
        del database[full_name]
        save_database(database)
        print(f"Запись '{full_name}' успешно удалена.")
    else:
        print(f"Запись '{full_name}' не найдена в базе данных.")

#Функция для поиска записей по строке поиска
def search_entry(database, query):
    found_entries = {}
    for key, value in database.items():
        if query.lower() in key.lower() or query.lower() in value['specialist'].lower() or query.lower() in value['policy_number'].lower():
            found_entries[key] = value
    return found_entries

def main():
    database = load_database()
    
    while True:
        print("Добро пожаловать в программу регистрации посетителей поликлиники!")
        print("Выберите действие:")
        print("1. Просмотреть базу данных")
        print("2. Добавить запись")
        print("3. Удалить запись")
        print("4. Найти запись")
        print("5. Выйти из программы")
        
        choice = input("Введите номер действия: ")
        
        if choice == "1":
            print_database(database)
        elif choice == "2":
            full_name = input("Введите Ф.И.О. больного: ")
            specialist = input("Введите принимающего специалиста: ")
            appointment_time = input("Введите время приема: ")
            policy_number = input("Введите номер полиса: ")
            add_entry(database, full_name, specialist, appointment_time, policy_number)
            print("Запись успешно добавлена в базу данных.")
        elif choice == "3":
            full_name = input("Введите Ф.И.О. больного для удаления: ")
            delete_entry(database, full_name)
        elif choice == "4":
            query = input("Введите строку для поиска: ")
            results = search_entry(database, query)
            print("Результаты поиска:")
            print_database(results)
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()