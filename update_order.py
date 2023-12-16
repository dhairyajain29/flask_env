from flask import Flask, request, jsonify
from db import get_db_connection  # Import your database connection function

app = Flask(__name__)

@app.route('/orders/<order_id>', methods=['PUT'])
def update_order(order_id):
    # Get the JSON data from the request
    data = request.json

    # Extract the data you want to update (assuming you want to update 'OrderName' and 'OrderDate')
    updated_order_name = data.get('OrderName')
    updated_order_date = data.get('OrderDate')

    # Check if both 'OrderName' and 'OrderDate' are provided in the request
    if updated_order_name is None or updated_order_date is None:
        return jsonify({"message": "Both 'OrderName' and 'OrderDate' are required for update"}), 400

    # Update the order in the database
    conn = get_db_connection()  # Establish a database connection

    if conn:
        try:
            cursor = conn.cursor()
            # Define the SQL query to update the order
            query = "UPDATE Order_Header SET OrderName = %s, OrderDate = %s WHERE OrderID = %s"
            cursor.execute(query, (updated_order_name, updated_order_date, order_id))
            conn.commit()
            cursor.close()
            conn.close()
            if cursor.rowcount == 0:
                return jsonify({"message": "Order not found"}), 404
            return jsonify({"message": "Order updated successfully"}), 200
        except Exception as e:
            return jsonify({"message": f"Failed to update order: {str(e)}"}), 500
    else:
        return jsonify({"message": "Database connection failed"}), 500

if __name__ == '__main__':
    app.run(debug=True)
