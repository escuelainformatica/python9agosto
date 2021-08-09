import pymssql
import os


# pandas = csv? excel? base?
# numpy = nd-array (listas)
# matplotlib = esa herramienta es para graficar.
# scikit = analisis

conn: pymssql.Connection = pymssql.connect("104.36.110.17", os.environ['usuariopython'], os.environ['claveypython'], "sales1")

cursor: pymssql.Cursor = conn.cursor(as_dict=True)

sql="""
SELECT sum(Sales.Quantity*Products.Price) total
FROM     Products INNER JOIN
                  Sales ON Products.ProductID = Sales.ProductID
where sales.CustomerID=%s
"""

numero_cliente=input("ingrese el numero del cliente")

cursor.execute(sql,(numero_cliente))

fila=cursor.fetchone() # devuelve 1 fila o cero si no hay datos

print(fila['total'])

