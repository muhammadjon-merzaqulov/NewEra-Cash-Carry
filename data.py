import sqlite3

def init_db():
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()

    # Users table
    cursor.execute(
        '''
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY UNIQUE NOT NULL,
                password TEXT NOT NULL,
                role TEXT NOT NULL
            )
        '''
    )

    # Products table
    cursor.execute(
        '''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                price REAL NOT NULL,
                quantity INTEGER NOT NULL,
                measure TEXT Not NULL
            )
        '''
    )

    # Orders table
    cursor.execute(
        '''
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                total_price REAL NOT NULL,
                FOREIGN KEY (username) REFERENCES users(username)
                )
        '''
    )

    # Order items table
    cursor.execute(
        '''
            CREATE TABLE IF NOT EXISTS order_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER NOT NULL,
            product_name TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL,
            measure TEXT NOT NULL,
            FOREIGN KEY (order_id) REFERENCES orders(id)
            )
        '''
    )

    conn.commit()
    conn.close()

init_db()

def insert_sample_data():
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()

    # Foydalanuvchilar uchun namunaviy ma'lumotlar
    users = [
        ("muhammadjon", "111", "superadmin"),
        ("shavkat", "222", "admin"),
        ("sanjar", "333", "customer")
    ]
    cursor.executemany("INSERT OR IGNORE INTO users (username, password, role) VALUES (?, ?, ?)", users)

    # Mahsulotlar uchun namunaviy ma'lumotlar
    products = [
        ("Non", 5000, 30, "dona"),
        ("Sut", 10000, 30, "litr"),
        ("Tuxum", 1500, 100, "dona"),
        ("Go'sht", 100000, 10, "kilo"),
        ("Qatiq", 10000, 10, "litr"),
        ("Piyoz", 3000, 50, "kilo")
    ]
    cursor.executemany("INSERT INTO products (name, price, quantity, measure) VALUES (?, ?, ?, ?)", products)

    conn.commit()
    conn.close()

insert_sample_data()