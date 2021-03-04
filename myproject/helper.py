import MySQLdb as mdb

class Helper():

    def __init__(self, test:str = "test"):
        self.test = test

    def get_obfapp_connection(self):
        obfapp_db = mdb.connect("localhost", "test", "test", "testdb")
        return obfapp_db

    def approve_status_update(self, qid, status):
        try:
            sql = "update backfill_queue set approved={} where qid={}".format(status, qid)
            self.execute_sql_obfapp(sql)
        except:
            self.log.info("nothing")
        return False

    def execute_sql_obfapp(self, sql):
        try:
            con = self.get_obfapp_connection()
            cur = con.cursor()
            cur.execute(sql)
            cur.close()
            con.commit()
            con.close()
        except Exception:
            raise("Failed to execute")
        return True
