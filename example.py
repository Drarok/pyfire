import pyfire

# Example use

# Set URL endpoint for Firebase realtime database
Pyfire = pyfire.Pyfire("https://tomi-firebase-test.firebaseio.com/")

# Post to the database in order to store object, ,ethod returns posted object upon successful insertion
# This will insert the object under a new unique ID.
# Read more about the IDL https://firebase.googleblog.com/2015/02/the-2120-ways-to-ensure-unique_68.html)
Pyfire.post({"post": "works"})

# Get objects from DB
print Pyfire.get()

# Set RELATIVE endpoint path (so path for request will be: https://tomi-firebase-test.firebaseio.com/users/tomi.json
Pyfire.set_endpoint_path("users/tomi")

# Get back value under new relative endpoint
print "Value for [users:tomi] is: " + Pyfire.get()