#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite


con = lite.connect('test.db')    

with con:

    # the contents of the Cars table using the dictionary cursor
    con.row_factory = lite.Row
       
    cur = con.cursor() 
    cur.execute("SELECT * FROM Cars")

    rows = cur.fetchall()

    for row in rows:
        print "%s %s %s" % (row["Id"], row["Name"], row["Price"])

