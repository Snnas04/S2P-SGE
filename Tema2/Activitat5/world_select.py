import psycopg2
import plotly.express as px

db_params = {
    "host": "localhost",
    "port": 5432,
    "user": "postgres",
    "password": "CalaClara21",
    "dbname": "world",
}

try:
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    # Consulta SQL para obtener el número de países por continente
    query = """
    SELECT continent, COUNT(*) AS num_countries
    FROM country
    GROUP BY continent
    ORDER BY continent;
    """
    cursor.execute(query)

    # Obtener los resultados de la consulta
    results = cursor.fetchall()

    # Cerrar la conexión
    cursor.close()
    conn.close()

    # Crear un DataFrame de los resultados
    import pandas as pd
    df = pd.DataFrame(results, columns=['Continent', 'NumCountries'])

    # Crear el histograma con Plotly
    fig = px.bar(df, x='Continent', y='NumCountries', title='Número de paisos per continent')
    fig.show()

except psycopg2.Error as e:
    print(f"Error: {e}")
