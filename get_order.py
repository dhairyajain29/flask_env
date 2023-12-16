from flask import Flask, jsonify
from db import get_db_connection  # Import your database connection function

app = Flask(__name__)

@app.route('/orders/<order_id>', methods=['GET'])
def get_order(order_id):
    # Establish a database connection
    conn = get_db_connection()
    
    if conn:
        try:
            cursor = conn.cursor(dictionary=True)
            # Define the SQL query to retrieve a specific order by order_id
            query = "SELECT * FROM Order_Header WHERE OrderID = %s"
            cursor.execute(query, (order_id,))
            order_data = cursor.fetchone()
            cursor.close()
            conn.close()
            if order_data:
                return jsonify(order_data), 200
            else:
                return jsonify({"message": "Order not found"}), 404
        except Exception as e:
            return jsonify({"message": f"Failed to retrieve order: {str(e)}"}), 500
    else:
        return jsonify({"message": "Database connection failed"}), 500

if __name__ == '__main__':
    app.run(debug=True)
