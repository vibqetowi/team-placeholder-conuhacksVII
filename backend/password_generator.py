# necessary imports
import secrets
import string
from faker import Faker 

class Password:

  f0 = Faker()
  Faker.seed(4321)
  
  print(f0.password())