import pyscopg2

#conexión a la base de datos
conexiom = pyscopg2.connect(
    host = "localhost",
    port= "5232"
    database = "credenciales",
    user = "Admin",
    password = "p4ssw0rdDB"
)

#crear cursos
cursor = conexion.cursor()
#ejecutar consulta 
cursor.execute("SELECT * FROM usuarios")
#fetchone() =una fila
#fetchmany (n) hasta n filas
registros = cursor.fatchall() #Recuperar todas las filas devueltas
#registros almacena en tuplas

for fila in registros: 
    print(fila)

    #cerrarla conexion 
    cursor.close()
    conexion.close()