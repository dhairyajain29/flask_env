from flask import Flask, request, jsonify
import mysql.connector
import datetime

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(user='root', password='root@123', host='localhost', database='datamodel')

@app.route('/create_order', methods=['POST'])
def create_order():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()

    # Default values
    currency_uom_id = data.get('currencyUomId', 'USD')
    status_id = data.get('statusId', 'OrderPlaced')

    # Required parameters
    order_name = data['orderName']
    placed_date = data['placedDate']  # Format: "YYYY-MM-DD"

    query = """INSERT INTO Order_Header (ORDER_NAME, CURRENCY_UOM_ID, STATUS_ID, PLACED_DATE) 
               VALUES (%s, %s, %s, %s)"""
    cursor.execute(query, (order_name, currency_uom_id, status_id, placed_date))
    conn.commit()

    order_id = cursor.lastrowid
    cursor.close()
    conn.close()

    return jsonify({'orderId': order_id}), 201

if __name__ == '__main__':
    app.run(debug=True)
