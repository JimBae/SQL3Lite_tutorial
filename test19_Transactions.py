#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
A transaction is an atomic unit of database operations against the data in one or more databases. The effects of all the SQL statements in a transaction can be either all committed to the database or all rolled back.

In SQLite, any command other than the SELECT will start an implicit transaction. Also, within a transaction a command like CREATE TABLE ..., VACUUM, PRAGMA, will commit previous changes before executing.

Manual transactions are started with the BEGIN TRANSACTION statement and finished with the COMMIT or ROLLBACK statements.

SQLite supports three non-standard transaction levels: DEFERRED, IMMEDIATE and EXCLUSIVE. SQLite Python module also supports an autocommit mode, where all changes to the tables are immediately effective.
'''

import sqlite3 as lite
import sys


try:
    con = lite.connect('test.db')
    cur = con.cursor()    
    cur.execute("DROP TABLE IF EXISTS Friends")
    cur.execute("CREATE TABLE Friends(Id INTEGER PRIMARY KEY, Name TEXT)")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Tom')")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Rebecca')")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Jim')")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Robert')")
    
    # We create a Friends table and try to fill it with data. However, as we will see, the data is not committed
    #con.commit()
            
except lite.Error, e:
    
    if con:
        con.rollback()
    
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:
    
    if con:
        con.close()


