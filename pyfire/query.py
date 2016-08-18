class Query:
    pyfire = None
    path = ''
    query_params = {}

    def __init__(self, pyfire, path):
        self.pyfire = pyfire
        self.path = path

    def order_by(self, order_by):
        self.query_params["orderBy"] = order_by
        return self

    def equal_to(self, equal):
        self.query_params["equalTo"] = equal
        return self

    def get(self):
        return self.pyfire.get(self.path, self.query_params)

