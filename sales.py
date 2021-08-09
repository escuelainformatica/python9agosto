import pymssql
import os

# pandas = csv? excel? base?
# numpy = nd-array (listas)
# matplotlib = esa herramienta es para graficar.
# scikit = analisis

conn: pymssql.Connection = pymssql.connect("104.36.110.17", os.environ['usuariopython'], os.environ['claveypython'], "sales1")

cursor: pymssql.Cursor = conn.cursor(as_dict=True)

sql="""
SELECT Sales.SalesID, Sales.SalesPersonID, Sales.CustomerID, Sales.ProductID, Sales.Quantity, Sales.Date, Products.Name, Products.Price
    FROM Products 
    INNER JOIN Sales ON Products.ProductID = Sales.ProductID
where Sales.CustomerID=%s                  
"""

numero_cliente=input("ingrese el numero del cliente")


cursor.execute(sql,(numero_cliente))

sales=cursor.fetchall()

cursor.close()
conn.close()

# {'SalesID': 1, 'SalesPersonID': 17, 'CustomerID': 10482, 'ProductID': 500, 'Quantity': 500, 'Date': datetime.datetime(2007, 1, 1, 0, 1)}
# for sale in sales:
#    print(sale)

total:int=0
for sale in sales:
    total=total+ (sale['Quantity']*sale['Price'])

# printf
print("total %.2f" % (total))
print("total {0}".format(total))
print(f"total {total}")
print("total "+str(total))


# str() = string
# int() = entero
# float() = flotante
# tuple() = tuple
# list() = lista






