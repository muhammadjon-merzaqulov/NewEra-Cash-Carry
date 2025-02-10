from users import Admin, Customer, SuperAdmin


def admin_menu(username):
    admin = Admin(username)
    while True:
        print("\nAdmin menyusi:")
        print("1. Mahsulotlar ro‘yxatini ko‘rish")
        print("2. Mahsulot qo‘shish")
        print("3. Mahsulotni yangilash")
        print("4. Mahsulotni o‘chirish")
        print("5. Buyurtmalarni ko‘rish")
        print("6. Chiqish")
        print("7. Tizimdan chiqish")
        choice = input("Tanlovingizni kiriting: ")
        if choice == "1":
            admin.view_products()
        elif choice == "2":
            name = input("Mahsulot nomini kiriting: ")
            price = float(input("Mahsulot narxini kiriting: "))
            quantity = int(input("Mahsulot miqdorini kiriting: "))
            measure = input("Mahsulot miqdorini kiriting: ")
            admin.add_product(name, price, quantity, measure)
        elif choice == "3":
            product_id = int(input("Yangilash uchun mahsulot ID ni kiriting: "))
            admin.update_product(product_id)
        elif choice == "4":
            product_id = int(input("O‘chirish uchun mahsulot ID ni kiriting: "))
            admin.delete_product(product_id)
        elif choice == "5":
            admin.view_orders()
        elif choice == "6":
            print("Admin menyusidan chiqilmoqda...")
            break
        elif choice == "7":
            print("Chiqilmoqda...")
            exit()
        else:
            print("Noto‘g‘ri tanlov. Qaytadan tanlov kiriting.")


def customer_menu(username):
    customer = Customer(username)
    while True:
        print("\nCustomer menyusi:")
        print("1. Mahsulotlar ro‘yxatini ko‘rish")
        print("2. Savatchaga mahsulot qo‘shish")
        print("3. Savatchadagi mahsulotlarni ko‘rish")
        print("4. Savatdan mahsulot olib tashlash")
        print("5. Buyurtma berish")
        print("6. Chiqish")
        print("7. Tizimdan chiqish")
        choice = input("Tanlovingizni kiriting: ")
        if choice == "1":
            customer.view_products()
        elif choice == "2":
            product_id = int(input("Mahsulot ID: "))
            quantity = int(input("Miqdorni kiriting: "))
            customer.add_to_cart(product_id, quantity)
        elif choice == "3":
            customer.view_cart()
        elif choice == "4":
            product_name = input("Mahsulot nomi: ")
            customer.remove_from_cart(product_name)
        elif choice == "5":
            print("Buyurtma muvaffaqiyatli bajarildi!")
            customer.place_order()
        elif choice == "6":
            print("Customer menyusidan chiqilmoqda...")
            break
        elif choice == "7":
            print("Chiqilmoqda...")
            exit()
        else:
            print("Noto‘g‘ri tanlov. Qaytadan tanlov kiriting.")


def superadmin_menu(username):
    superadmin = SuperAdmin(username)
    while True:
        print("\nSuperadmin menyusi:")
        print("1. Admin qo‘shish")
        print("2. Foydalanuvchilar va Adminlar ro‘yxatini ko‘rish")
        print("3. Foydalanuvchini yangilash")
        print("4. Foydalanuvchini o‘chirish")
        print("5. Admin vazifalarini qilish")
        print("6. Chiqish")
        print("7. Tizimdan chiqish")
        choice = input("Tanlovingizni kiriting: ")
        if choice == "1":
            username = input("Login kiriting: ")
            password = input("Parol kiriting: ")
            superadmin.add_admin(username, password)
        elif choice == "2":
            superadmin.view_users()
        elif choice == "3":
            username = input("Yangilash uchun login kiriting: ")
            superadmin.update_user(username)
        elif choice == "4":
            username = input("O‘chirish uchun login kiriting: ")
            superadmin.delete_user(username)
        elif choice == "5":
            admin_menu(username)
        elif choice == "6":
            print("Superadmin menyusidan chiqilmoqda...")
            break
        elif choice == "7":
            print("Chiqilmoqda...")
            exit()
        else:
            print("Noto‘g‘ri tanlov. Qaytadan tanlov kiriting.")