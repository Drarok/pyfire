from pyfire import Pyfire
import config

# Set URL endpoint and secret key to the Firebase realtime database
fb = Pyfire(config.FIREBASE_DATABASE_URL, config.FIREBASE_DATABASE_SECRET)

# Create an object in the Test collection
id = fb.post('Test', {'Foo': 'Bar'})

# Get the random key generated for the above object (can be used to add further
# children), then replace everything under this key
fb.put('Test/' + id, {'bar': 'foo'})

# Add a new object. This does not overrite existing children, but just appends this one
fb.patch('Test/' + id, {'more': 'data'})

# Get the contents.
print fb.get('Test/' + id)

# Get objects by querying - you will need to set up .indexOn for this to work
try:
    print fb.query('Test').order_by('bar').equal_to('foo').get()
except Exception as e:
    print e

# Delete the object we created
fb.delete('Test/' + id)
