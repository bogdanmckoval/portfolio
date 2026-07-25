import json
import os
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
FILE_NAME = SCRIPT_DIR / 'contacts.json'


def save_contacts(contacts):
    with open(FILE_NAME, 'w', encoding='utf-8') as file:
        json.dump(contacts, file, ensure_ascii=False, indent=2)


def load_contacts():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, 'r', encoding='utf-8') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def add_contact(contacts):
    print("\n--- Додавання нового контакту ---")
    name = input("Ім'я: ").strip()
    if not name:
        print("Ім'я не може бути порожнім!")
        return
    if any(c['name'].lower() == name.lower() for c in contacts):
        print("Контакт з таким ім'ям уже існує!")
        return

    phone = input("Телефон: ").strip()
    email = input("Email: ").strip()
    address = input("Адреса: ").strip()

    contacts.append({
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    })
    save_contacts(contacts)
    print(f"Контакт '{name}' додано успішно!")


def view_all_contacts(contacts):
    if not contacts:
        print("\nСписок контактів порожній!")
        return
    print("\n--- Усі контакти ---")
    for i, contact in enumerate(contacts, 1):
        print(f"\n{i}. {contact['name']}")
        if contact.get('phone'):
            print(f"   Телефон: {contact['phone']}")
        if contact.get('email'):
            print(f"   Email: {contact['email']}")
        if contact.get('address'):
            print(f"   Адреса: {contact['address']}")


def search_contact(contacts):
    print("\n--- Пошук контакту ---")
    query = input("Введіть ім'я або телефон: ").strip().lower()

    results = [c for c in contacts
               if query in c['name'].lower()
               or query in c.get('phone', '').lower()]

    if not results:
        print("Контактів не знайдено!")
        return

    print(f"\nЗнайдено {len(results)} контакт(ів):")
    for contact in results:
        print(f"\n- {contact['name']}")
        if contact.get('phone'):
            print(f"  Телефон: {contact['phone']}")
        if contact.get('email'):
            print(f"  Email: {contact['email']}")
        if contact.get('address'):
            print(f"  Адреса: {contact['address']}")


def edit_contact(contacts):
    print("\n--- Редагування контакту ---")
    name = input("Введіть ім'я контакту: ").strip()

    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print("\n1. Ім'я\n2. Телефон\n3. Email\n4. Адреса\n0. Вихід")
            choice = input("Виберіть поле: ").strip()

            if choice == '1':
                contact['name'] = input("Нове ім'я: ").strip()
            elif choice == '2':
                contact['phone'] = input("Новий телефон: ").strip()
            elif choice == '3':
                contact['email'] = input("Новий email: ").strip()
            elif choice == '4':
                contact['address'] = input("Нова адреса: ").strip()
            elif choice == '0':
                return
            else:
                print("Невірний вибір!")
                return

            save_contacts(contacts)
            print("Контакт оновлено!")
            return

    print("Контакт не знайдено!")


def delete_contact(contacts):
    print("\n--- Видалення контакту ---")
    name = input("Введіть ім'я контакту для видалення: ").strip()

    for i, contact in enumerate(contacts):
        if contact['name'].lower() == name.lower():
            deleted = contacts.pop(i)
            save_contacts(contacts)
            print(f"Контакт '{deleted['name']}' видалено!")
            return

    print("Контакт не знайдено!")

def main():
    print("=== Менеджер контактів ===")

    while True:
        contacts = load_contacts()

        print("\n--- Головне меню ---")
        print(f"Всього контактів: {len(contacts)}")
        print("1. Перегляд усіх контактів")
        print("2. Додати новий контакт")
        print("3. Пошук контакту")
        print("4. Редагувати контакт")
        print("5. Видалити контакт")
        print("0. Вихід")

        choice = input("\nВиберіть дію: ").strip()

        if choice == '1':
            view_all_contacts(contacts)
        elif choice == '2':
            add_contact(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            edit_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '0':
            print("\nДо побачення!")
            break
        else:
            print("Невірний вибір! Спробуйте ще раз.")


if __name__ == "__main__":
    main()