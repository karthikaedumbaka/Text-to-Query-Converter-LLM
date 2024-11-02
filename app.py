import streamlit as st
import pandas as pd
import openai
import pandasql as psql
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(dotenv_path='C:\\Users\\karth\\OneDrive\\Desktop\\bb\\.evn')


# Initialize OpenAI API key from environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")
if openai_api_key:
    openai.api_key = openai_api_key
    st.success('OpenAI API key loaded successfully.', icon="✅")
else:
    st.error("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")

def generate_sql_query(query, schema, dialect):
    # Construct the prompt for the OpenAI API
    prompt = f'Generate a "{dialect} + language" query for the following schema: {json.dumps(schema)}\nQuery: {query}\n:'
    print(dialect)
    # Call OpenAI API to get the SQL query
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"You are a helpful assistant that generates {dialect}."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5
    )
    
    sql_query = response.choices[0].message['content'].strip()
    # Remove any code block formatting
    sql_query = sql_query.replace('```sql', '').replace('```', '').strip()
    return sql_query

st.title('Text to Query Converter')

# File uploader for multiple CSV files
uploaded_files = st.file_uploader("Upload CSV files", accept_multiple_files=True)

# Text input for natural language query
query = st.text_input("Enter your query")

# Dropdown for SQL dialect selection
dialect = st.selectbox("Select SQL Dialect", ["MySQL", "Oracle", "PL/SQL", "SQL Server", "DB2", "PostgreSQL"])

# Container for uploaded tables
tables = {}
schema = {}

# Read uploaded files into Pandas DataFrames
if uploaded_files:
    for uploaded_file in uploaded_files:
        table_name = uploaded_file.name.split('.')[0]
        df = pd.read_csv(uploaded_file)
        tables[table_name] = df
        schema[table_name] = list(df.columns)

# Generate and execute SQL query
if st.button("Generate SQL Query"):
    if query and schema:
        sql_query = generate_sql_query(query, schema, dialect)
        st.write("Generated SQL Query:")
        st.code(sql_query, language='sql')
        
        try:
            result = psql.sqldf(sql_query, tables)
            st.write("Query Result:")
            st.dataframe(result)
        except Exception as e:
            st.error(f"Error executing query: {e}")
    else:
        st.error("Please upload CSV files and enter a query.")
