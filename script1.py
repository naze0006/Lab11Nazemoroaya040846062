#!/usr/bin/python
# -*- coding: utf-8 -*-

# Import modules  
import cgi, cgitb 
import sqlite3 as lite
import sys


# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
dateValue = str(form.getvalue('dateValue'))
timeValue  = str(form.getvalue('timeValue'))

con = lite.connect('readings.db')

with con:

    con.row_factory = lite.Row
    cur = con.cursor()
    #q = ("SELECT * FROM readings WHERE dateReading = '%s' and timeReading = '%s'" % (dateValue,timeValue))
    q = "SELECT * FROM Readings WHERE dateReading = " + "\"" + dateValue + "\"" + " AND  datetime (timeReading) >= datetime " + "(\"" + timeValue + " \" ,'-10 minutes') AND datetime (timeReading) <= datetime " + "(\""+ timeValue + "\" , '+10 minutes')"   
    print "Content-type:text/html\r\n\r\n"
    print "<html>"
    print "<head>"
    print "<title>Hello - CGI Program</title>"
    print "</head>"
    print "<body>"
    print "<div>"
    print "<table style='margin: 0 auto'>"
    print "<tr style='background-color:grey'><th>DATE</th><th>TIME</th><th>TEMPERATURE</th><th>HUMIDITY</th></tr>"

    cur.execute(q)
    rows = cur.fetchall()

    for row in rows:
	
	print "<tr>"
	print "<td style='border: 1px solid black;text-align:center'>%s</td>" % row["dateReading"]
        print "<td style='border: 1px solid black;text-align:center'>%s</td>" % row["timeReading"]
	print "<td style='border: 1px solid black;text-align:center'>%s</td>" % row["temperature"] 
	print "<td style='border: 1px solid black;text-align:center'>%s</td>" % row["humidity"]
        print "</tr>"
    print "</table>"
    print "</div>"
    print "</body>"
    print "</html>"

