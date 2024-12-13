import os
import pandas as pd
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Read CSV data
df = pd.read_csv(r"C:\Users\vivek\OneDrive\Desktop\intro python\loan_data_app\database\loan_data.csv")

# Example: If you want to use the SQLite database
conn = sqlite3.connect(r"C:\Users\vivek\OneDrive\Desktop\intro python\loan_data_app\database\loan_data.db")
cursor = conn.cursor()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/data')
def data():
    # Extract the column names and sample data from the DataFrame
    column_names = df.columns.tolist()
    rows = df.head(5).values.tolist()  # Display the first 5 rows as sample data
    description = {
        'Loan_ID': 'Unique identifier for each loan',
        'Gender': 'Gender of the applicant',
        'Married': 'Marital status of the applicant',
        'Dependents': 'Number of dependents of the applicant',
        'Education': 'Education level of the applicant',
        'Self_Employed': 'Whether the applicant is self-employed',
        'ApplicantIncome': 'Income of the applicant',
        'CoapplicantIncome': 'Income of the coapplicant',
        'LoanAmount': 'Requested loan amount',
        'Loan_Amount_Term': 'Term of the loan in months',
        'Credit_History': 'Credit history (1: Good, 0: Poor)',
        'Property_Area': 'Area where the property is located',
        'Loan_Status': 'Loan approval status (Y: Approved, N: Not Approved)'
    }
    return render_template('data.html', description=description, table_headers=column_names, table_data=rows)

if __name__ == '__main__':
    app.run(debug=True)
