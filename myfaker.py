import pandas as pd
from faker import Faker

# Create an Faker object
fake = Faker()

# Now you have many options to genarate data:
fake.name()
fake.text()
fake.address()
fake.email()
fake.date()
fake.country()
fake.phone_number()
fake.random_number(digits=5)

# let's generate an example DataFrame
faker_df = pd.DataFrame({'date':[fake.date() for i in range(10)],
                         'name':[fake.name() for i in range(10)],
                         'email':[fake.email() for i in range(10)],
                         'text':[fake.text() for i in range(10)]})
faker_df
