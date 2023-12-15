from lib.Request import Request


class RequestRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * from REQUESTS")
        requests = [
            Request(row["id"], row["status"], row["request_from"], row["request_to"])
            for row in rows
        ]
        return requests

    # Function returns a list of all requests with status null
    def all_null(self):
        rows = self._connection.execute("SELECT * from REQUESTS WHERE status IS NULL")
        requests = [
            Request(row["id"], row["status"], row["request_from"], row["request_to"])
            for row in rows
        ]
        return requests

    # Function returns a list of all requests with status true
    def all_true(self):
        rows = self._connection.execute("SELECT * from REQUESTS WHERE status = true")
        requests = [
            Request(row["id"], row["status"], row["request_from"], row["request_to"])
            for row in rows
        ]
        return requests

    # Function returning a status of request between session user and accesed profile user
    # For custom reject/accept/contact details/send request button
    # “” -> “send request”
    # None -> “accept or reject”
    # True -> “match”
    # False -> “rejected”

    def get_request_status(self, session_user_id, profile_user_id):
        rows = self._connection.execute(
            "SELECT * from REQUESTS WHERE request_from = %s and request_to = %s",
            [session_user_id, profile_user_id],
        )
        if rows == []:
            return ""
        else:
            return rows[0]["status"]
