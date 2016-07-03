import urllib2
import json


class Pyfire:

    def __init__(self, url, secret=None):
        if not url.endswith('/'):
            self.root_data_url = ''.join([url, '/'])
        else:
            self.root_data_url = url
        self.endpoint_path = ''
        self.auth_token = None
        self.database_secret = secret # Create database secrets here: https://console.firebase.google.com/ => Select your project => Click settings wheel in top left => Project Settings => Database => Add Secret
        self.query_params = {}

    def get_endpoint_path(self):
        return self.endpoint_path

    def set_endpoint_path(self, endpoint_path):
        self.endpoint_path = endpoint_path
        return self

    def get_database_secret(self):
        return self.database_secret

    def set_database_secret(self, secret):
        self.database_secret = secret
        return self

    # GET - Reading data
    # The response will contain all the data under the specified endpoint path
    def get(self):
        return self._execute("GET", {})

    # PUT - Writing Data:
    # This will override everything under the current working path with the object specified
    def put(self, data):
        return self._execute("PUT", data)

    # POST - Pushing Data
    # This will create a new object at the current path with a new unique key.
    # The response will contain the newly created object (along with its generated key (its 'name' attribute)
    def post(self, data):
        return self._execute("POST", data)

    # PATCH - Updating Data
    # We can update specific children at a location without overwriting existing data using a PATCH request.
    # Named children in the data being written with PATCH will be overwritten, but omitted children will not be deleted.
    # A successful request will be indicated by a 200 OK HTTP status code. The response will contain the data written:
    def patch(self, data):
        return self._execute("PATCH", data)

    # DELETE - Removing Data
    # Deletes everyhing under the current path
    def delete(self):
        return self._execute("DELETE", {})

    def order_by(self, order_by):
        self.query_params["orderBy"] = order_by
        return self

    def equal_to(self, equal):
        self.query_params["equalTo"] = equal
        return self

    def _execute(self, request_method, data):
        request_url = self.root_data_url + self.endpoint_path + '.json?'
        query_string = None

        if self.database_secret:
            request_url += 'auth=' + self.database_secret

        if self.query_params:
            query_string = "&"
            if self.query_params.get('orderBy'):
                query_string += 'orderBy=\"'+self.query_params.get('orderBy')+'\"'
                # Can only use equalTo with orderBy, so nest if statement
                if self.query_params.get('equalTo'):
                    query_string += '&equalTo=\"'+self.query_params.get('equalTo')+'\"'

        if query_string:
            request_url += query_string

        headers = {}
        data_json = json.dumps(data)

        headers.update({'X-HTTP-Method-Override': request_method.upper()})  # TODO: explain reasoning for why I use this
        headers.update({'Content-Type': 'application/json'})

        req = urllib2.Request(request_url, data_json, headers)
        response = urllib2.urlopen(req).read()

        return response
