import sqlite3

conn = sqlite3.connect("store.db")

############################################################################################################
def get_role(username, password):
    """
    Foydalanuvchi login va parolini tekshirish.
    """
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT role FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        if user:
            return user[0]
    except:
        return False

def have_user(username):
    """
    Bunday login tizimda mavjudligini tekshirish.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    return user

def add_user(username, password, role='customer'):
    """
    Yangi user qo'shadi agar 3-argni bermasa customer deb qo'shadi
    """
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, password, role))
        conn.commit()
        return f"Yangi user: ({username}) ({role}) rolida muvaffaqiyatli qo‘shildi!"
    except sqlite3.IntegrityError:
        return "Bunday login allaqachon mavjud."
    except Exception as e:
        return e

def view_products():
    """
    Barcha mahsulotlarni ko'rish
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    return products

def have_product(product_id):
    """product_id bo'yicha product borligini tekshiradi"""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
        result = cursor.fetchone()
        return result
    except Exception as e:
        return f"Xato yuz berdi: {e}"

def add_product(name, price, quantity, measure):
    """
    Mahsulot qo'shish
    """
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO products (name, price, quantity, measure) VALUES (?, ?, ?)", (name, price, quantity, measure))
        conn.commit()
        return f"Mahsulot ({name}) muvaffaqiyatli qo‘shildi!"
    except sqlite3.IntegrityError:
        return "Bunday mahsulot allaqachon mavjud."
    except Exception as e:
        return e

def update_product_price(product_id, price):
    """
    Mahsulot narxini yangilash
    """
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
        product = cursor.fetchone()
        if product:
            cursor.execute("UPDATE products SET price = ? WHERE id = ?", (price, product_id))
            conn.commit()
            return f"({product[1]}) narxi muvaffaqiyatli yangilandi!"
        else:
            return "Bunday mahsulot topilmadi."
    except Exception as e:
        return e

def update_product_quantity(product_id, quantity):
    """
    Mahsulot miqdorini yangilash
    """
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
        product = cursor.fetchone()
        if product:
            cursor.execute("UPDATE products SET quantity = ? WHERE id = ?", (quantity, product_id))
            conn.commit()
            return f"({product[1]}) miqdori ({product[3]}) taga muvaffaqiyatli yangilandi!"
        else:
            return "Bunday mahsulot topilmadi."
    except Exception as e:
        return e

def update_product_measure(product_id, measure):
    """
    Mahsulot miqdorini yangilash
    """
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
        product = cursor.fetchone()
        if product:
            cursor.execute("UPDATE products SET measure = ? WHERE id = ?", (measure, product_id))
            conn.commit()
            return f"({product[1]}) measuri ({product[4]})ga muvaffaqiyatli yangilandi!"
        else:
            return "Bunday mahsulot topilmadi."
    except Exception as e:
        return e


def delete_product(product_id):
    """
    Mahsulotni o'chirish
    """
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
        product = cursor.fetchone()
        if product:
            cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
            conn.commit()
            return f"({product[1]}) muvaffaqiyatli o'chirildi!"
        else:
            return "Bunday mahsulot topilmadi."
    except Exception as e:
        return e


def add_order(username, total_price):
    """
    Buyurtma qo'shish
    """
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO orders (username, total_price) VALUES (?, ?)", (username, total_price))
        conn.commit()
        return f"Buyurtma muvaffaqiyatli qo‘shildi!"
    except sqlite3.IntegrityError:
        return "Bunday buyurtma allaqachon mavjud."
    except Exception as e:
        return e

def get_order_id(username):
    """
    Buyurtma ID sini olish
    """
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM orders WHERE username = ?", (username,))
    order_id = cursor.fetchone()
    return order_id[0]

def add_order_items(order_id, product_name, price, quantity, measure):
    """
    Order item qo'shish
    """
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO order_items (order_id, product_name, price, quantity, measure) VALUES (?, ?, ?, ?)", (order_id, product_name, price, quantity, measure))
        conn.commit()
        return f"Order item ({product_name}) muvaffaqiyatli qo‘shildi!"
    except sqlite3.IntegrityError:
        return "Bunday order item allaqachon mavjud."
    except Exception as e:
        return e

def view_orders_with_items():
    """
    Foydalanuvchilarning buyurtmalarini ko'rish
    """
    try:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM orders")
        orders = cursor.fetchall()

        if not orders:
            return "Hech qanday buyurtma mavjud emas."

        result = ""  # Natijalarni yig'ish uchun
        for order_id, username, total_price in orders:
            result += f"Mijozning ismi: {username}\n"
            result += "Mahsulotlar:\n"

            cursor.execute("SELECT * FROM order_items WHERE order_id = ?", (order_id,))
            order_items = cursor.fetchall()

            if not order_items:
                result += "  - Buyurtmaga hech qanday mahsulot kiritilmagan.\n"
            else:
                for product_name, price, quantity, measure in order_items:
                    result += f"  - {product_name}: ${price:.2f} x {quantity} {measure}\n"

            result += f"Umumiy narx: ${total_price:.2f}\n"
            result += "-" * 30

        return result

    except Exception as e:
        return f"Xato yuz berdi: {e}"



def view_users(role='superadmin'):
    """
    Foydalanuvchilarni ko'rish.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users where role <> ?", (role,))
    users = cursor.fetchall()
    return users

def delete_user(username):
    """
    Foydalanuvchini o'chirish
    """
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        if user:
            cursor.execute("DELETE FROM users WHERE username = ?", (username,))
            conn.commit()
            return f"Foydalanuvchi ({username}) muvaffaqiyatli o'chirildi!"
        else:
            return "Bunday foydalanuvchi topilmadi."
    except Exception as e:
        return e

def update_user(username, role):
    """
    Foydalanuvchini yangilash
    """
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        if user:
            cursor.execute("UPDATE users SET role = ? WHERE username = ?", (role, username))
            conn.commit()
            print(f"Foydalanuvchi ({username}) ({role}) roliga muvaffaqiyatli yangilandi!")
        else:
            print("Bunday foydalanuvchi topilmadi.")
    except Exception as e:
        return e

