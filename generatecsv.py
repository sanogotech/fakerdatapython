from faker import Faker
from faker.providers import DynamicProvider


# To create a json file
import json        
import csv
from random import randint       
  
fake = Faker()
#'hi_IN' changed the language


    


def input_dataCSV(x): 
  
    header = ['enabled', 'full_name', 'password', 'username']
    listData= []
    for i in range(0, x):
    
        oneDataLine = [randint(0, 1), fake.name(), fake.md5(), fake.last_name()]
        listData.append(oneDataLine)
    
    print(listData)

    with open('users.csv', 'w+', encoding='UTF8') as myfile:
            writer = csv.writer(myfile)

            # write the header
            writer.writerow(header)

            # write the data
            writer.writerows(listData)    



def main():
    print("hello world  Faker ...!")
    print(" ------------------------------------------ \n")
    input_dataCSV(5)

if __name__ == "__main__":
    main()