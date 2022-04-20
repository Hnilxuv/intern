import pyodbc

conx_string = "driver={SQL Server Native Client 11.0}; server=DESKTOP-09AHFD3; database=ex3; trusted_connection=YES;"

cnx = pyodbc.connect(conx_string)
cursor = cnx.cursor()
# cnx = pyodbc.connect(Trusted_Connection='yes',
#                      Driver='{SQL Server Native Client 11.0}',
#                      Server='DESKTOP-09AHFD3',
#                      Database='ex3')