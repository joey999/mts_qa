import atexit, copy
import psycopg2
from settings import configEnv


class PsqlClient(object):
    def __init__(self):
        self.connection = None
        self.cursor = None
        self.psql = configEnv['psql']

        atexit.register(self.close())

    def _create_connection_master(self):
        master = copy.deepcopy(self.psql)
        master['database'] = 'master'
        self.connection = psycopg2.connect(**master)
        return self.connection

    def _create_cursor(self):
        self.cursor = self.connection.cursor()
        return self.cursor

    def create_snapshot(self):
        pass

    def delete_snapshot(self):
        pass

    def restore_snapshot(self):
        pass

    def query(self, query):
        self._create_connection_master()
        self._create_cursor()

        try:
            self.cursor.execute(query)
            res = self.cursor.fetchall()
            self.connection.commit()
            return res
        except Exception:
            raise Exception("Error with query execution")

    def close(self):
        if self.cursor:
            self.cursor.close()

        if self.connection:
            self.connection.close()
