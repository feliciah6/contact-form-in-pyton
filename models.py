from peewee import (CharField,
                    SqliteDatabase,
                    Model,
                    TextField,
                    IntegerField,
                    OperationalError,
                    IntegrityError)
db = SqliteDatabase("contact.db")
contacts = [
    {'id': 1,'email': 'john@doe.com', 'name': 'felician','phone':'0712282129'},
    {'id': 2,'email': 'john@doe.com', 'name': 'felician','phone':'0712282129'}
    
    
    
]



class Contact(Model):
    
    
    email = CharField(max_length=100)
    name = CharField(max_length=100)
    phone=IntegerField(default=10)

    class Meta:
        database = db

def initialize():
    try:
        Contact.create_table()
    except OperationalError:
        pass
    for contact in contacts:
      try:
        Contact.create(
            email=contact.get('email'),
            name=contact.get('name'),
            phone=contact.get('0712282129'),
           
            )
      except IntegrityError:
        pass
    


