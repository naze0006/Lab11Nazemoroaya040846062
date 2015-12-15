#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite


con = lite.connect('readings.db')    

with con:
    
    con.row_factory = lite.Row
       
    cur = con.cursor() 
    cur.execute("SELECT * FROM readings")

    rows = cur.fetchall()

    for row in rows:
        print "%s %s %s %s %s"  % (row["id"], row["dateReading"], row["timeReading"], row["temperature"], row["humidity"])
