#!/bin/env python3

import mysql.connector

connection = mysql.connector.connect(user = 'root', database = 'pokemon', password = 'password')

cursor = connection.cursor()

testQuery = ("SELECT * FROM pokemon")

cursor.execute(testQuery)

for item in cursor:
    print(item) 

cursor.close()

connection.close()