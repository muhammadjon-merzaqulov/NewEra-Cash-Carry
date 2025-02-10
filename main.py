import sqlite3
from menu import admin_menu, customer_menu, superadmin_menu
import query as q


def main():
    conn = sqlite3.connect("store.db")
    print("Tizimga xush kelibsiz!")
    try:
        while True:
            username = input("Loginni kiriting: ")
            if q.have_user(username):
                password = input("Parolni kiriting: ")
            else:
                print("Bunday login tizimda mavjud emas.")
                choice = input("Yangi mijoz yaratmoqchimisiz? (y/n): ").strip().lower()
                if choice == "y":
                    password = input("Parolni kiriting: ")
                    q.add_user(username, password)
                    continue
                else:
                    print("Qaytadan login kiritishingiz mumkin.")
                    continue

            role = q.get_role(username, password)
            if not role:
                print("Parol xato. Qaytadan urinib ko'ring.")
                continue

            if role == "customer":
                customer_menu(username)
            elif role == "admin":
                admin_menu(username)
            elif role == "superadmin":
                superadmin_menu(username)
    finally:
        conn.close()


if __name__ == "__main__":
    main()




