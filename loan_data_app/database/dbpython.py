import pandas as pd
import sqlite3

# Load the data from CSV file
file_path = r'C:\Users\vivek\OneDrive\Desktop\intro python\loan_data_app\database\loan_data.csv'
df = pd.read_csv(file_path)

# Create a connection to SQLite database (this will create the file if it doesn't exist)
conn = sqlite3.connect('loan_data.db')

# Save the DataFrame to SQLite database as a new table (you can replace 'loan_data' with a name you prefer)
df.to_sql('loan_data', conn, if_exists='replace', index=False)

# Close the connection
conn.close()

print("Database 'loan_data.db' created successfully and data imported.")
