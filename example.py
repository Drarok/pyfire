import pyfire
import pyfire.utils as utils
import config

# Example use of Pyfire

# Set URL endpoint and secret key (respectively) to the Firebase realtime database
Pyfire = pyfire.Pyfire(config.FIREBASE_DATABASE_URL, config.FIREBASE_DATABASE_SECRET)

new_object = Pyfire.post({'Foo': 'Bar'}) # Post an object to the Firebase realtime database. The object will be assigned an unique key. EG: "-KLYFXcwUO-rKJMwrT0F" and the stored object is returned
new_object_name = utils.get_property_from_json_string('name', new_object) # Get the random key generated for the above object (can be used to add further children by changing the relative path to this)

Pyfire.set_endpoint_path(new_object_name) # Set path to the key of the item just created

Pyfire.put({'bar': 'foo'})  # Puts a new object into current path. This overrides(deletes) everything under this key

Pyfire.patch({'more': 'data'})  # Add a new object into current path. This does not overrite existing children, but just appends this one

print Pyfire.set_endpoint_path('').get()  # Set endpoint path back to the root and get the contents. (This line demonstrates how certain request can be chained)
