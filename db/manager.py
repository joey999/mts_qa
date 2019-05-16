from db.client import PsqlClient


class DBManager(object):
    def __init__(self):
        self.db = PsqlClient()

    def query(self, query_body):
        return self.db.query(query_body)

    def query_example(self):
        return self.db.query('''select * from auth_Roles''')

    def create_snapshot(self):
        return self.db.create_snapshot()

    def restore_from_snapshot(self):
        return self.db.restore_snapshot()

    def delete_snapshot(self):
        return self.db.delete_snapshot()


db_manager = DBManager()
