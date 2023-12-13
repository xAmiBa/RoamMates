class Request:

    def __init__(self, id, status, request_from, request_to):
        self.id = id
        self.status = status
        self.request_from = request_from
        self.request_to = request_to

    def __eq__(self, other):
        return self.__dict__ == other.__dict__