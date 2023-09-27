import psycopg2

# Parámetros de conexión a la base de datos PostgreSQL
db_host = 'localhost'     # Cambia esto por la dirección del servidor de tu base de datos
# Cambia esto por el puerto de tu base de datos (por defecto, PostgreSQL usa el puerto 5432)
db_port = '5432'
db_name = 'mysvalenciagdb'  # Cambia esto por el nombre de tu base de datos
db_user = 'svalenciag'    # Cambia esto por tu nombre de usuario de PostgreSQL
db_password = 'password'  # Cambia esto por tu contraseña de PostgreSQL

try:
    # Conectar a la base de datos
    connection = psycopg2.connect(
        host=db_host,
        port=db_port,
        database=db_name,
        user=db_user,
        password=db_password
    )

    # Crear un cursor
    cursor = connection.cursor()

    # Ejecutar consultas SQL o realizar otras operaciones aquí

    # Ejemplo: Ejecutar una consulta
    cursor.execute("""SELECT * FROM datosanillo WHERE radio_anillo = '100'""")

    # Obtener resultados
    for row in cursor:
        print(row)

    # Cerrar el cursor y la conexión
    cursor.close()
    connection.close()

except psycopg2.Error as e:
    print(f'Error de PostgreSQL: {str(e)}')
