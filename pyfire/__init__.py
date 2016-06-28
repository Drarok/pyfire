import urllib2
import json

class Pyfire:

    def __init__(self, url):
        self.root_data_url = url
        self.endpoint_path = ''

    def get_endpoint_path(self):
        return self.endpoint_path

    def set_endpoint_path(self, endpoint_path):
        self.endpoint_path = endpoint_path

    # GET - Reading data
    # Data from our Firebase database can be read by issuing an HTTP GET request to an endpoint:
    # A successful request will be indicated by a 200 OK HTTP status code.
    # The response will contain the data being retrieved:
    # { "first": "foo", "last": "bar" }
    def get(self):
        return self._execute("GET", {})


    # PUT - Writing Data
    # We can write data with a PUT request:
    # A successful request will be indicated by a 200 OK HTTP status code. The response will contain the data written:
    def put(self, data):
        return self._execute("PUT", data)

    # POST - Pushing Data
    # To accomplish the equivalent of the JavaScript push() method (see Lists of Data), we can issue a POST request:
    # A successful request will be indicated by a 200 OK HTTP status code.
    # The response will contain the child name of the new data that was added:
    def post(self, data):
        return self._execute("POST", data)

    # PATCH - Updating Data
    # We can update specific children at a location without overwriting existing data using a PATCH request.
    # Named children in the data being written with PATCH will be overwritten, but omitted children will not be deleted.
    # This is equivalent to the JavaScript update() function.
    # A successful request will be indicated by a 200 OK HTTP status code. The response will contain the data written:
    def patch(self, data):
        return self._execute("PATCH", data)

    # DELETE - Removing Data
    # We can delete data with a DELETE request:
    # A successful DELETE request will be indicated by a 200 OK HTTP status code with a response containing JSON null.
    def delete(self):
        return self._execute("DELETE", {})

    def _execute(self, request_method, data):
        request_url = self.root_data_url + self.endpoint_path + '/.json'

        headers = {}
        data_json = json.dumps(data)

        headers.update({'X-HTTP-Method-Override': request_method.upper()}) # TODO: explain reasoning for why I use this
        headers.update({'Content-Type': 'application/json'})

        req = urllib2.Request(request_url, data_json, headers)

        response = urllib2.urlopen(req).read()

        return response

