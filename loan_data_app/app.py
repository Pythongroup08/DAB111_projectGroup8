import os
import sqlite3
import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

# Base directory of the project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Path to the database and CSV files
DATABASE_PATH = os.path.join(BASE_DIR, "database", "loan_data.db")
CSV_PATH = os.path.join(BASE_DIR, "database", "loan_data.csv")

# Load data from CSV
df = pd.read_csv(CSV_PATH)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    description = {
        "Loan_ID": "Unique Loan ID",
        "Gender": "Gender of the applicant",
        # Add descriptions for all columns
    }
    dataset_source = "https://www.kaggle.com/datasets/taweilo/loan-approval-classification-data"
    return render_template("about.html", description=description, dataset_source=dataset_source)

@app.route("/data")
def data():
    column_names = df.columns.tolist()
    rows = df.values.tolist()
    
    # Define column descriptions
    description = {
        "Loan_ID": "Unique Loan ID",
        "Gender": "Gender of the applicant",
        "Married": "Marital status of the applicant",
        "Dependents": "Number of dependents",
        "Education": "Education level of the applicant",
        "Self_Employed": "Self-employment status",
        "ApplicantIncome": "Income of the applicant",
        "CoapplicantIncome": "Income of the co-applicant",
        "LoanAmount": "Amount of loan applied for",
        "Loan_Amount_Term": "Loan repayment term",
        "Credit_History": "Credit history of the applicant",
        "Property_Area": "Area of property",
        "Loan_Status": "Loan status (Approved/Rejected)"
    }
    
    return render_template(
        "data.html", 
        table_headers=column_names, 
        table_data=rows[:5], 
        description=description
    )


if __name__ == "__main__":
    app.run(debug=True)
