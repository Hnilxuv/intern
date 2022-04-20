import pyodbc

conx_string = "driver={SQL Server Native Client 11.0}; server=DESKTOP-09AHFD3; database=ex1; trusted_connection=YES;"

cnxn = pyodbc.connect(conx_string)
cursor = cnxn.cursor()