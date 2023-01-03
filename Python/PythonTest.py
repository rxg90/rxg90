# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 15:01:04 2023

@author: rxg15259
"""
import jaydebeapi
import jpype
import os

#DRIVER_PATH= "./CI_CD/tools/drivers/jdbc/denodo-vdp-jdbcdriver-8.0-ga.jar"

#jpype.shutdownJVM()

driver_class = 'com.microsoft.sqlserver.jdbc.SQLServerDriver'
driver_path = ".\mssql-jdbc-11.2.1.jre8.jar"


url = 'jdbc:sqlserver://covxus6sqldwserverdevtest001.database.windows.net:1433;database=vx-vxdev-sqldw-001;integratedSecurity=true;useNTLMv2=true'
user = 'df135747'
password = '5phjS&btxQSsAwz'


#jpype.startJVM(jpype.getDefaultJVMPath(), "-Djava.class.path=" + driver_path)

# Establish the connection
conn = jaydebeapi.connect(driver_class, url, [user, password])

# Create a cursor
cursor = conn.cursor()

# Execute a query
cursor.execute("SELECT name FROM sys.objects WHERE type_desc = 'USER_TABLE'")

# Fetch the results
results = cursor.fetchall()

# Print the results
for row in results:
    print(row)

# Close the connection
conn.close()
