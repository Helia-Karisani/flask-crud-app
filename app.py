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

# Delete operation

# Run the Flask app
    