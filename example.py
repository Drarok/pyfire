import pyfire
import config

# Set URL endpoint and secret key (respectively) to the Firebase realtime database
Pyfire = pyfire.Pyfire(config.FIREBASE_DATABASE_URL, config.FIREBASE_DATABASE_SECRET)

# Create an object in the Test collection
id = Pyfire.post('Test', {'Foo': 'Bar'})

# Get the random key generated for the above object (can be used to add further
# children), then replace everything under this key
Pyfire.put('Test/' + id, {'bar': 'foo'})

# Add a new object. This does not overrite existing children, but just appends this one
Pyfire.patch('Test/' + id, {'more': 'data'})

# Get the contents.
print Pyfire.get('Test/' + id)

# Get objects by querying - you will need to set up .indexOn for this to work
try:
    print Pyfire.query('Test').order_by('bar').equal_to('foo').get()
except Exception as e:
    print e

# Delete the object we created
Pyfire.delete('Test/' + id)
