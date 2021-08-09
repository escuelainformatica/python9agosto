import pymssql
import os

conn = pymssql.connect("104.36.110.17", os.environ['usuariopython'], os.environ['claveypython'], "MilkCo")

cursor:pymssql.Cursor=conn.cursor(as_dict=True)

# cursor: pymssql.Cursor = conn.cursor(as_dict=True)

cursor.execute("select * from cities")

ciudades=cursor.fetchall()

# {'idCity': 4658, 'name': 'Mongu', 'idCountry': 221, 'population': 52534, 'lastUpdate': datetime.datetime(2020, 6, 21, 14, 17, 23)}

for ciudad in ciudades:
    print("No={0},Nombre={1}".format(ciudad['idCity'],ciudad['name']))











