from flask import Flask, request, jsonify
from db import get_db_connection  # Import your database connection function

app = Flask(__name__)

@app.route('/create_orders', methods=['POST'])
def create_order():
    # Get the JSON data from the request
    data = request.json

    # Check if the required fields are present in the request data
    if 'OrderName' not in data or 'OrderDate' not in data:
        return jsonify({"message": "Missing required fields"}), 400

    # Extract the data from the request
    order_name = data['OrderName']
    order_date = data['OrderDate']

    # Insert the order into the database
    conn = get_db_connection()  # Establish a database connection

    if conn:
        try:
            cursor = conn.cursor()
            # Define the SQL query to insert the order
            query = "INSERT INTO Order_Header (OrderName, OrderDate) VALUES (%s, %s)"
            cursor.execute(query, (order_name, order_date))
            conn.commit()
            cursor.close()
            conn.close()
            return jsonify({"message": "Order created successfully"}), 201
        except Exception as e:
            return jsonify({"message": f"Failed to create order: {str(e)}"}), 500
    else:
        return jsonify({"message": "Database connection failed"}), 500

if __name__ == '__main__':
    app.run(debug=True)
