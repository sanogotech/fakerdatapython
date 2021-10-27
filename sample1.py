
from faker import Faker

# To create a json file
import json        
  
# For student id 
from random import randint       
  
fake = Faker()
#'hi_IN' changed the language

  
def input_dataJson(x): 
  
    # dictionary 
    student_data ={} 
    for i in range(0, x): 
        student_data[i]={} 
        student_data[i]['id']= randint(1, 100) 
        student_data[i]['name']= fake.name() 
        student_data[i]['address']= fake.address() 
        student_data[i]['latitude']= str(fake.latitude()) 
        student_data[i]['longitude']= str(fake.longitude()) 
    print(student_data) 
  
    # dictionary dumped as json in a json file 
    with open('students.json', 'w') as fp: 
        json.dump(student_data, fp) 


def  uniqueValuesInt():
    for _ in range(10):
        print(fake.unique.random_int())

def  uniqueValuesNames():

    fake = Faker()
    names = [fake.unique.first_name() for i in range(10)]
    assert len(set(names)) == len(names)
    print(names)

def printName():

    fake = Faker('fr_FR')
    for seq in range(10):
        print(fake.name())

def printEmailName():
    #fake = Faker('hi_IN')
    #fake = Faker('en_US')
    fake = Faker('fr_FR') 
       


    print (fake.email())
    print(fake.country())
    print(fake.name())
    print(fake.text())
    print(fake.latitude(), fake.longitude())
    print(fake.url())

def printSequenceWord(): 
    # List has words that we want in our sentence 
    word_list = ["GFG", "Geeksforgeeks","shaurya", "says", "Gfg","GEEKS"] 
      
    # Let's print 5 sentences that
    # have words from our word_list 
    for i in range(0, 5): 
        # You need to use ext_word_list = listnameyoucreated 
        print(fake.sentence(ext_word_list = word_list)) 

def main():
    print("hello world  Faker ...!")
    #printEmailName()
    #printName()
    uniqueValuesNames()
    input_dataJson(2)
    printSequenceWord()

if __name__ == "__main__":
    main()