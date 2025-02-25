import csv
import re
from pprint import pprint

# Чтение адресной книги
with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# Функция для приведения ФИО к правильному формату
def fix_names(contacts):
    for contact in contacts:
        full_name = " ".join(contact[:3]).split(" ")
        contact[:3] = list(map(lambda i: full_name[i] if i < len(full_name) else "", range(3)))
    return contacts

# Функция для приведения телефонов к единому формату
def fix_phones(contacts):
    phone_pattern = re.compile(
        r"(\+7|8)\s*\(?(\d{3})\)?[\s-]?(\d{3})[\s-]?(\d{2})[\s-]?(\d{2})(\s*\(?(доб\.?)\s*(\d+)\)?)?"
    )
    for contact in contacts:
        phone = contact[5]
        if phone:
            match = phone_pattern.match(phone)
            if match:
                formatted_phone = f"+7({match.group(2)}){match.group(3)}-{match.group(4)}-{match.group(5)}"
                if match.group(7):
                    formatted_phone += f" доб.{match.group(8)}"
                contact[5] = formatted_phone
    return contacts

# Функция для объединения дублирующихся записей
def merge_duplicates(contacts):
    unique_contacts = {}
    for contact in contacts:
        key = (contact[0], contact[1])
        if key in unique_contacts:
            existing_contact = unique_contacts[key]
            for i in range(len(contact)):
                if not existing_contact[i] and contact[i]:
                    existing_contact[i] = contact[i]
        else:
            unique_contacts[key] = contact
    return list(unique_contacts.values())

# Применяем функции для обработки данных
contacts_list = fix_names(contacts_list)
contacts_list = fix_phones(contacts_list)
contacts_list = merge_duplicates(contacts_list)

# Сохранение результата в новый файл
with open("phonebook.csv", "w", encoding="utf-8", newline="") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list)

# Вывод результата для проверки
pprint(contacts_list)