#!/usr/bin/python
# -*- coding: utf-8 -*-

# Import modules  
import cgi, cgitb 
import sqlite3 as lite
import sys


# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
dateValue = form.getvalue('dateValue')
timeValue  = form.getvalue('timeValue')




con = lite.connect('readings.db')

with con:

    cur = con.cursor()
    cur.execute("SELECT * FROM readings WHERE dateReading = dateValue & timeReading = timeValue")

    while True:

        row = cur.fetchone()

        if row == None:
            break

        print row[0], row[1], row[2], row[3], row[4]


print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Hello - CGI Program</title>"
print "</head>"
print "<body>"
print "<h2>received from the form %s %s</h2>" % (dateValue, timeValue)
print "</body>"
print "</html>"

