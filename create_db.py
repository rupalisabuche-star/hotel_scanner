import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Hotels table
cursor.execute('''CREATE TABLE IF NOT EXISTS hotels (
    id INTEGER PRIMARY KEY,
    name TEXT,
    address TEXT,
    contact TEXT,
    instagram TEXT,
    photo TEXT
)''')

# Menu table
cursor.execute('''CREATE TABLE IF NOT EXISTS menu (
    id INTEGER PRIMARY KEY,
    hotel_id INTEGER,
    dish_name TEXT,
    price REAL,
    photo TEXT
)''')

# Orders table
cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY,
    name TEXT,
    table_no TEXT,
    items TEXT
)''')

# Sample hotel
cursor.execute("INSERT INTO hotels (name,address,contact,instagram,photo) VALUES (?,?,?,?,?)",
               ("Star Hotel","Main Road, Pune, India","+91 9876543210","@starhotel","/static/hotel.jpg"))

# Sample menu
cursor.execute("INSERT INTO menu (hotel_id,dish_name,price,photo) VALUES (?,?,?,?)",
               (1,"Paneer Butter Masala",250,"/static/dish1.jpg"))
cursor.execute("INSERT INTO menu (hotel_id,dish_name,price,photo) VALUES (?,?,?,?)",
               (1,"Margherita Pizza",300,"/static/dish2.jpg"))

conn.commit()
conn.close()