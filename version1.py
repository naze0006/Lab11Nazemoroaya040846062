#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

db = lite.connect('readings.db')
with db:

    cur = db.cursor()
    cur.execute("SELECT * FROM readings")

    rows = cur.fetchall()
 
    for row in rows:
        print(row)

