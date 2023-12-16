from flask import Flask, jsonify
from db import get_db_connection  # Import your database connection function

app = Flask(__name__)

@app.route('/orders', methods=['GET'])
def get_all_orders():
    # Establish a database connection
    conn = get_db_connection()
    
    if conn:
        try:
            cursor = conn.cursor(dictionary=True)
            # Define the SQL query to retrieve all orders
            query = "SELECT * FROM Order_Header"
            cursor.execute(query)
            orders_data = cursor.fetchall()
            cursor.close()
            conn.close()
            return jsonify(orders_data), 200
        except Exception as e:
            return jsonify({"message": f"Failed to retrieve orders: {str(e)}"}), 500
    else:
        return jsonify({"message": "Database connection failed"}), 500

if __name__ == '__main__':
    app.run(debug=True)
