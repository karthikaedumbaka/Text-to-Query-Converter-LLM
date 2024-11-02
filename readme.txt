Text to Query Converter
This project is a Streamlit-based application that converts natural language input into SQL queries using OpenAI's GPT model. It allows users to upload CSV files, enter a natural language query, and choose an SQL dialect to generate and execute an SQL query. The app provides an intuitive interface for non-technical users to query their data without directly writing SQL.

Features
Natural Language to SQL Conversion: Converts user-provided text queries to SQL.
SQL Dialect Selection: Supports multiple SQL dialects, including MySQL, Oracle, PL/SQL, SQL Server, DB2, and PostgreSQL.
File Upload: Supports uploading multiple CSV files to define the data schema.
Automatic SQL Execution: Executes generated SQL queries using pandasql and displays the results in a table.
Requirements
Python 3.8 or higher
Packages:
streamlit
pandas
openai
pandasql
python-dotenv

Install the required packages:
pip install -r requirements.txt

Usage
Start the Streamlit app:
bash
Copy code
streamlit run app.py
In the app interface:
Upload one or more CSV files to define your schema.
Enter a natural language query.
Choose the desired SQL dialect.
Click the "Generate SQL Query" button to generate and execute the SQL query.
File Structure
app.py: Main application code.
.env: Stores environment variables (OpenAI API key).
requirements.txt: Lists dependencies for the project.
Example
Upload a CSV file named employees.csv.
Enter a natural language query, such as "Get all employees with a salary above 50,000.".
Select your desired SQL dialect (e.g., MySQL).
Click "Generate SQL Query" to see the query and results.