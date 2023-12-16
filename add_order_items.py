from flask import Flask, request, jsonify
from db import get_db_connection  # Import your database connection function

app = Flask(__name__)

@app.route('/orders/<order_id>/items', methods=['POST'])
def add_order_items(order_id):
    # Get the JSON data from the request
    data = request.json

    # Check if the required fields are present in the request data
    if 'ItemName' not in data or 'Quantity' not in data:
        return jsonify({"message": "Missing required fields"}), 400

    # Extract the data from the request
    item_name = data['ItemName']
    quantity = data['Quantity']

    # Insert the item into the Order_Part table associated with the specified order_id
    conn = get_db_connection()  # Establish a database connection

    if conn:
        try:
            cursor = conn.cursor()
            # Define the SQL query to insert the item into Order_Part
            query = "INSERT INTO Order_Part (OrderID, ItemName, Quantity) VALUES (%s, %s, %s)"
            cursor.execute(query, (order_id, item_name, quantity))
            conn.commit()
            cursor.close()
            conn.close()
            return jsonify({"message": "Items added to order successfully"}), 201
        except Exception as e:
            return jsonify({"message": f"Failed to add items to order: {str(e)}"}), 500
    else:
        return jsonify({"message": "Database connection failed"}), 500

if __name__ == '__main__':
    app.run(debug=True)
