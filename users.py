import query as q


class Cart:
    """
    Savat klassi. Savatdagi mahsulotlarni saqlash va boshqarish uchun metodlar mavjud.
    """
    def __init__(self):
        self.items = {}

    def add_to_cart(self, product_name, price, quantity, measure):
        """
        Savatga mahsulot qo‘shish.
        """
        if product_name in self.items:
            self.items[product_name]["quantity"] += quantity
        else:
            self.items[product_name] = {"price": price, "quantity": quantity, "measure": measure}

    def view_cart(self):
        """
        Savatni ko‘rish.
        """
        if not self.items:
            print("Savat bo‘sh.")
        else:
            print("\nSavatdagi mahsulotlar:")
            for product_name, details in self.items.items():
                print(f"{product_name} - ${details['price']:.2f} x {details['quantity']} {details['measure']}")
            print(f"Umumiy summa: ${self.calculate_total():.2f}")

    def calculate_total(self):
        """
        Savatdagi mahsulotlarning umumiy summasini hisoblash.
        """
        return sum(details["price"] * details["quantity"] for details in self.items.values())

    def clear_cart(self):
        """
        Savatni tozalash.
        """
        self.items = {}

    def remove_from_cart(self, product_name):
        """
        Savatchadan mahsulot olib tashlash.
        """
        if product_name in self.items:
            del self.items[product_name]
            print(f"{product_name} savatchadan o'chirildi!")
        else:
            print("Mahsulot topilmadi.")

class Admin:
    """"
    Admin klassi. Bu klass mahsulotlarni boshqaradi.
    """
    def __init__(self, username):
        self.username = username

    def view_products(self):
        """
        Mahsulotlarni ko'rish.
        """
        products = q.view_products()
        print("\nMahsulotlar:")
        for id, name, price, quantity, measure in products:
            print(f"{id}. {name} - ${price:.2f} ({quantity} {measure})")
        print("-" * 30)

    def add_product(self, name, price, quantity, measure):
        """
        Mahsulot qo‘shish.
        """
        print(q.add_product(name, price, quantity, measure))

    def update_product(self, product_id):
        """
        Mahsulotni yangilash.
        """
        product = q.have_product(product_id)
        if product:
            print(f"Tanlangan mahsulot: {product[1]} - ${product[2]:.2f} "
                  f"({product[3]} {product[4]} mavjud)")

            print("\nQaysi xususiyatni o‘zgartirmoqchisiz?")
            print("1. Narxni o‘zgartirish")
            print("2. Miqdorni o‘zgartirish")
            print("3. Measuri(kg, dona)ni o‘zgartirish")
            print("4. 3 lasini ham o‘zgartirish")
            choice = input("Tanlovingizni kiriting (1/2/3): ")

            if choice == "1":
                try:
                    new_price = float(input("Yangi narxni kiriting: "))
                    print(q.update_product_price(product_id, new_price))
                except:
                    print("Narxni noto‘g‘ri kiritdingiz.")
            elif choice == "2":
                try:
                    new_quantity = int(input("Yangi miqdorni kiriting: "))
                    print(q.update_product_quantity(product_id, new_quantity))
                except:
                    print("Miqdorni noto‘g‘ri kiritdingiz.")
            elif choice == "3":
                try:
                    new_measure = input("Yangi measurini kiriting: ")
                    print(q.update_product_measure(product_id, new_measure))
                except:
                    print("Measurini noto‘g‘ri kiritdingiz.")
            elif choice == "4":
                new_price = float(input("Yangi narxni kiriting: "))
                new_quantity = int(input("Yangi miqdorni kiriting: "))
                new_measure = input("Yangi measurini kiriting: ")
                print(q.update_product_price(product_id, new_price))
                print(q.update_product_quantity(product_id, new_quantity))
                print(q.update_product_measure(product_id, new_measure))
            else:
                print("Noto‘g‘ri tanlov. Yangilash bekor qilindi.")
        else:
            print("Mahsulot topilmadi.")

    def delete_product(self, product_id):
        """
        Mahsulotni o'chirish.
        """
        if q.have_product(product_id):
            print(q.delete_product(product_id))
        else:
            print("Mahsulot topilmadi.")

    def view_orders(self):
        """
        Buyurtmalarni ko'rish.
        """
        print("\nBuyurtmalar:")
        print(q.view_orders_with_items())

class Customer:
    """
    Customer klassi. Bu klass mijozlar uchun mahsulotlarni ko'rish, savatchaga mahsulot qo'shish, savatni ko'rish, buyurtma berish va boshqa amallarni bajarish uchun metodlar mavjud.
    """
    def __init__(self, username):
        self.username = username
        self.cart = Cart()

    def view_products(self):
        """
        Mahsulotlarni ko'rish.
        """
        products = q.view_products()
        print("\nMahsulotlar:")
        for id, name, price, quantity, measure in products:
            print(f"{id}. {name} - ${price:.2f} ({quantity} {measure})")
        print("-" * 30)

    def add_to_cart(self, product_id, quantity):
        """
        Savatchaga mahsulot qo‘shish.
        """
        product = q.have_product(product_id)
        if product:
            if quantity <= product[3]:
                self.cart.add_to_cart(product[1], product[2], quantity, product[4])
                q.update_product_quantity(product_id, product[3] - quantity)
                print(f"{quantity} {product[4]} - '{product[1]}' savatga qo‘shildi!")
            else:
                print("Yetarli mahsulot mavjud emas.")

    def view_cart(self):
        """
        Savatchani ko'rish.
        """
        self.cart.view_cart()

    def remove_from_cart(self, product_name):
        self.cart.remove_from_cart(product_name)

    def place_order(self):
        """
        Buyurtma berish.
        """
        if not self.cart.items:
            print("Savat bo‘sh.")
            return
        else:
            total_price = self.cart.calculate_total()
            print(f"Umumiy summa: ${total_price:.2f}")
            confirm = input("Buyurtmani tasdiqlaysizmi? (y/n): ")
            if confirm.lower() == "y":
                q.add_order(self.username, total_price)
                order_id = q.get_order_id(self.username)
                for product_name, details in self.cart.items.items():
                    q.add_order_items(order_id, product_name, details["price"], details["quantity"], details["measure"])
                self.cart.clear_cart()
                print("Buyurtma qabul qilindi!")
            else:
                print("Buyurtma bekor qilindi.")

class SuperAdmin:
    """
    Super admin. Bu klass eng kattasi bo'lib ham Adminlarni ham Customerlarni boshqaradi
    """
    def __init__(self, username):
        self.username = username

    def add_admin(self, username, password):
        """
        Admin qo‘shish.
        """
        print(q.add_user(username, password, 'admin'))

    def view_users(self):
        """
        Foydalanuvchilarni ko'rish.
        """
        users = q.view_users()
        i = 1
        print("\nFoydalanuvchilar:")
        for username, password, role in users:
            print(f"{i}. {username.title()} ({role})")
            i += 1


    def delete_user(self, username):
        """
        Foydalanuvchi o'chirish.
        """
        print(q.delete_user(username))

    def update_user(self, username):
        """
        Foydalanuvchini yangilash.
        """
        user = q.have_user(username)
        if user:
            print(f"Tanlangan foydalanuvchi: {username} ({user[2]})")
            new_role = input("Yangi rolni kiriting (admin/customer): ")
            if new_role not in ["admin", "customer"]:
                print("Noto‘g‘ri rolni kiritdingiz.")
            else:
                q.update_user(username, new_role)
        else:
            print("Foydalanuvchi topilmadi.")





