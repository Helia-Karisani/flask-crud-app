# Import libraries
from flask import Flask, jsonify, request, url_for, redirect, render_template
#from flask import <functions>

# Instantiate Flask functionality
app = Flask(__name__)

# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

# Read operation
@app.route("/")
def get_transactions():
    return render_template('transactions.html', transactions=transactions)

# Create operation
#GET for displaying the form to the user and POST for processing the form data sent by the user
@app.route("/add", methods=['GET', 'POST'])
def add_transaction():
    if request.method == 'POST':
        # Create a new transaction object using form field values
        new_transaction = {
            #Generate a new ID based on the current length of the transactions list
            'id': len(transactions) + 1,
            'date': request.form['date'],
            #Get the 'amount' field value from the form and convert it to a float
            'amount': float(request.form['amount'])
        }
        transactions.append(new_transaction)
        return redirect(url_for('get_transactions'))
    return render_template('add_transaction.html')


# Update operation
#GET for displaying the current transaction data in a form, and POST for processing the updated data sent by the user
@app.route("/edit/<int:transaction_id>", methods=['GET', 'POST'])
def edit_transaction(transaction_id):
    if request.method == 'POST':
        # Extract the updated values from the form fields
        date = request.form['date']           # Get the 'date' field value from the form
        amount = float(request.form['amount'])# Get the 'amount' field value from the form and convert it to a float

        # Find the transaction by ID and update its values
        for transaction in transactions:
            if transaction['id'] == transaction_id:
                transaction['date'] = date
                transaction['amount'] = amount
                break
        return redirect(url_for('get_transactions'))
    # if the request method is GET, find the transaction by ID and display its current values in the form
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            return render_template('edit.html', transaction=transaction)
    return {"message": "Transaction not found"}, 404

# Delete operation
@app.route("/delete/<int:transaction_id>", methods=['POST'])
def delete_transaction(transaction_id):
    # Find the transaction with the matching ID and remove it from the list
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            transactions.remove(transaction)  # Remove the transaction from the transactions list
            break  # Exit the loop once the transaction is found and removed
    # Redirect to the transactions list page after deleting the transaction
    return redirect(url_for("get_transactions"))

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
# The app will run in debug mode, which is useful for development and debugging purposes
# The debug mode will automatically reload the server when code changes are made
# and will provide detailed error messages in the browser if any errors occur.
    