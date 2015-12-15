#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = lite.connect('readings.db')

with con:
    
    cur = con.cursor()    
    cur.execute("SELECT * FROM readings")

    while True:
      
        row = cur.fetchone()
        
        if row == None:
            break
            
        print row[0], row[1], row[2], row[3], row[4]
