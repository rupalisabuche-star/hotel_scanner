from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Home page with scanner
@app.route('/')
def index():
    return render_template('index.html')

# After scan, show hotel info
@app.route('/hotel/<hotel_id>')
def hotel(hotel_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM hotels WHERE id=?", (hotel_id,))
    hotel = cursor.fetchone()
    
    cursor.execute("SELECT * FROM menu WHERE hotel_id=?", (hotel_id,))
    menu = cursor.fetchall()
    
    conn.close()
    return render_template('hotel.html', hotel=hotel, menu=menu)

# Place order
@app.route('/order', methods=['POST'])
def order():
    name = request.form['name']
    table_no = request.form['table']
    items = request.form.getlist('items')
    
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO orders (name, table_no, items) VALUES (?, ?, ?)",
                   (name, table_no, ",".join(items)))
    conn.commit()
    conn.close()
    
    return render_template('order_success.html', name=name, items=items)

if __name__ == '__main__':
    app.run(debug=True)
    import qrcode

img = qrcode.make("https://hotel-scanner.onrender.com")
img.save("qr.png")
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)