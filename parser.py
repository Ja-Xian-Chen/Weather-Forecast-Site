#!/bin/python
import sys
import mysql.connector
import xml.dom.minidom

doc = xml.dom.minidom.parse(sys.argv[1])
if sys.argv[1][20:22]=="NY":
    state = "New York"
elif sys.argv[1][20:22]=="CA":
    state = "California"
elif sys.argv[1][20:22]=="IL":
    state = "Illinois"
elif sys.argv[1][20:22]=="TX":
    state = "Texas"
elif sys.argv[1][20:22]=="AZ":
    state = "Arizona"
elif sys.argv[1][20:22]=="PA":
    state = "Pennsylvania"
elif sys.argv[1][20:22]=="FL":
    state = "Florida"
dstate = state

city = doc.getElementsByTagName("h2")[0]
dcity = city.firstChild.data

temp = doc.getElementsByTagName("p")[4]
dtemp = temp.firstChild.data

date =  sys.argv[1][:10]
ddate=date

short1 = doc.getElementsByTagName("p")[8]
shortDesc1 = doc.getElementsByTagName("p")[10]

short2 = doc.getElementsByTagName("p")[12]
shortDesc2 = doc.getElementsByTagName("p")[14]

short3 = doc.getElementsByTagName("p")[16]
shortDesc3 = doc.getElementsByTagName("p")[18]

short4 = doc.getElementsByTagName("p")[20]
shortDesc4 = doc.getElementsByTagName("p")[22]

short5 = doc.getElementsByTagName("p")[24]
shortDesc5 = doc.getElementsByTagName("p")[26]

short6 = doc.getElementsByTagName("p")[28]
shortDesc6 = doc.getElementsByTagName("p")[30]

short7 = doc.getElementsByTagName("p")[32]
shortDesc7 = doc.getElementsByTagName("p")[34]

short8 = doc.getElementsByTagName("p")[36]
shortDesc8 = doc.getElementsByTagName("p")[38]

short9 = doc.getElementsByTagName("p")[40]
shortDesc9 = doc.getElementsByTagName("p")[42]

shortDescription = "{}:{}\n{}:{}\n{}:{}\n{}:{}\n{}:{}\n{}:{}\n{}:{}\n{}:{}\n{}:{}".format(short1.firstChild.data, shortDesc1.firstChild.data,short2.firstChild.data, shortDesc2.firstChild.data,short3.firstChild.data,shortDesc3.firstChild.data,short4.firstChild.data,shortDesc4.firstChild.data,short5.firstChild.data,shortDesc5.firstChild.data,short6.firstChild.data,shortDesc6.firstChild.data,short7.firstChild.data,shortDesc7.firstChild.data,short8.firstChild.data,shortDesc8.firstChild.data,short9.firstChild.data,shortDesc9.firstChild.data)

data = mysql.connector.connect(
  host="localhost",
  user="root",
  database= "data"
)

mycursor = data.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS " + dstate + " (state VARCHAR(255),city VARCHAR(255), date DATE, daynight VARCHAR(255), temperture INT(255), shortDesc VARCHAR(255), longDesc VARCHAR(255))")


sql = "REPLACE INTO " + dstate + " (state, city, date, daynight, temperture, shortDesc, longDesc) VALUES (%s, %s, %s, %s, %s, %s, %s);"
val = (dstate, dcity, ddate, None, None,shortDescription,None)

mycursor.execute(sql, val)
data.commit()
