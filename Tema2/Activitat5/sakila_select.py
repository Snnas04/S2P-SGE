import mysql.connector

# Establece la conexión a la base de datos sakila
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="CalaClara21",
    database="sakila",  # Nombre de la base de datos sakila
    port=3307  # Puerto de MySQL (ajusta según tu configuración)
)

# Verifica si la conexión se ha establecido correctamente
if mydb.is_connected():
    print("Conexión exitosa")

# Crea un cursor para ejecutar consultas
cursor = mydb.cursor()

# Define la consulta SQL que deseas ejecutar
sql_query = """
SELECT COUNT(category_id), category_id
FROM film_category
GROUP BY category_id;
"""

# Ejecuta la consulta
cursor.execute(sql_query)

# Obtiene los resultados de la consulta
results = cursor.fetchall()

# Imprime los resultados
for row in results:
    count, category_id = row
    print(f"Categoría {category_id}: {count} películas")

# Cierra el cursor y la conexión
cursor.close()
mydb.close()
