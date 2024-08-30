import os
from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()

# 1) Connect to the database here using the SQLAlchemy's create_engine function
DATABASE_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
engine = create_engine(DATABASE_URL)

# 2) Execute the SQL sentences to create your tables using the SQLAlchemy's execute function
with engine.connect() as connection:
    with open('./src/sql/create.sql', 'r') as file:
        create_sql = file.read()
    connection.execute(text(create_sql))
    print("Tables created successfully.")

# 3) Execute the SQL sentences to insert your data using the SQLAlchemy's execute function
with engine.connect() as connection:
    with open('./src/sql/insert.sql', 'r') as file:
        insert_sql = file.read()
    connection.execute(text(insert_sql))
    print("Data inserted successfully.")

# 4) Use pandas to print one of the tables as dataframes using read_sql function
table_name = "your_table_name"  # Replace with the actual table name you want to print
df = pd.read_sql(f"SELECT * FROM {table_name};", engine)
print(f"Data from {table_name}:")
print(df)

