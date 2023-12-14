from lib.Request import Request

class RequestRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from REQUESTS')
        requests = [Request(row["id"], row["status"], row["request_from"], row["request_to"]) for row in rows]
        return requests