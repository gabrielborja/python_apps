import sqlite3

class Database:
    """Create a database to handle CRUD operations for the operational log"""

    def __init__(self, db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS op_log (id INTEGER PRIMARY KEY, date text, name text, shift text, machine text, comments text)")
        self.conn.commit()

    def insert(self, date, name, shift, machine, comments):
        self.cur.execute("INSERT INTO op_log VALUES (NULL,?,?,?,?,?)",(date, name, shift, machine, comments))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM op_log")
        rows=self.cur.fetchall()
        return rows

    def search(self, date="", name="", shift="", machine="", comments=""):
        self.cur.execute("SELECT * FROM op_log WHERE date=? OR name=? OR shift=? OR machine=? OR comments=?", (date, name, shift, machine, comments))
        rows=self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM op_log WHERE id=?",(id,))
        self.conn.commit()

    def update(self, id, date, name, shift, machine, comments):
        self.cur.execute("UPDATE log_op SET date=?, name=?, shift=?, machine=?, comments=? WHERE id=?",(date, name, shift, machine, comments,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
