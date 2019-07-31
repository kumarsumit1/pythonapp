from pyspark.sql import SparkSession
spark = SparkSession\
        .builder\
        .getOrCreate()

import random
import string


def randomRegistration(stringLength=8):
    """Generate a random registration string of fixed length """
    letters= string.ascii_lowercase
    return ''.join(random.sample(letters,stringLength))

def randomEngineSize():
    """Generate a random Engine Size of fixed length """
    letters= string.digits
    return '1.'+random.sample(letters,1)[0]         

def randomPrice():
    """Generate a random Engine price"""
    letters= string.digits
    return 500+ int(''.join(random.sample(letters,4)))         
  
makeModelList =[("FORD", "FIESTA"),
       ("NISSAN", "QASHQAI"),
       ("HYUNDAI", "I20"),
       ("SUZUKI", "SWIFT") ,
       ("MERCEDED_BENZ", "E CLASS"),
       ("VAUCHALL", "CORSA"),
       ("FIAT", "500"),
       ("SKODA", "OCTAVIA"),
       ("KIA", "RIO") ]

def randomMakeModel():
    if (random.random() < 0.6) :
      return makeModelList[0]
    else :
      return makeModelList[random.randrange(1,len(makeModelList))] 
    
print(random.choice([True, False]))

print(makeModelList[len(makeModelList)-1])
print(random.randrange(1,len(makeModelList)))