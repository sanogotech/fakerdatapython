import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

#dialect+driver://username:password@host:port/database
# default
#engine = create_engine('postgresql://scott:tiger@localhost/mydatabase')
# psycopg2
#engine = create_engine('postgresql+psycopg2://scott:tiger@localhost/mydatabase')
# pg8000
#engine = create_engine('postgresql+pg8000://scott:tiger@localhost/mydatabase')
# Create the engine to connect to a MYSQL database
# default
engine = create_engine('mysql+pymysql://root@localhost/powerball')

# Read data from the SQL Table
data = pd.read_csv('users.csv')

# Print first few rows of the dataframe
print(data.head())

#######################################################################################

# Write the data into a table in PostgreSQL Database

data.to_sql(name = 'users',
            con = engine,
            if_exists='append',
            index = False
)


"""
data.to_sql(name = 'users',
            con = engine,
            if_exists='append',
            index = False,
            chunksize = 1000,
            
            dtype = {
                "Row_ID" : sqlalchemy.types.Integer,
                "Order_ID" : sqlalchemy.types.Text,
                "Order_Date" : sqlalchemy.types.DateTime,
                "Ship_Date" : sqlalchemy.types.DateTime,
                "Sales" : sqlalchemy.types.Numeric,
                "Quantity" : sqlalchemy.types.Integer,
                "Discount" : sqlalchemy.types.Numeric,
                "Profit" : sqlalchemy.types.Numeric,
            }
)

"""